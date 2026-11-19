import json
import os
import random
import secrets
import time
from datetime import timedelta
from flask import Flask, render_template, request, session, redirect, jsonify

app = Flask(__name__)
NUM_QUESTIONS_PER_QUIZ = 5
QUESTION_TIME_LIMIT = 20
SPEED_BONUS_LIMIT = 5
QUESTIONS_FILE = os.path.join(app.root_path, "Question.json")
SCORES_FILE = os.path.join(app.root_path, "Scores.json")


# Keep the same key so the app can remember returning players.
key_file = os.path.join(app.root_path, "secret_key.txt")
if not os.path.exists(key_file):
    with open(key_file, "w", encoding="utf-8") as file:
        file.write(secrets.token_hex(32))

with open(key_file, "r", encoding="utf-8") as file:
    app.secret_key = file.read().strip()

app.permanent_session_lifetime = timedelta(days=30)
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"


# Load the questions and check the file format.
# ChatGPT helped check the JSON format and fix the options/answers lookup.
def load_questions():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
        questions = json.load(file)
    if not isinstance(questions, dict) or len(questions) < NUM_QUESTIONS_PER_QUIZ:
        raise ValueError("Question.json must have at least five questions.")
    for question, item in questions.items():
        if not isinstance(question, str) or not question.strip() or not isinstance(item, dict):
            raise ValueError
        options = item.get("options")
        answers = item.get("answers")
        if not isinstance(options, list) or len(options) < 2:
            raise ValueError("Each question needs at least two options.")
        for option in options:
            if not isinstance(option, str) or not option.strip():
                raise ValueError("All answer options must be nonempty text.")
        if len(set(options)) != len(options):
            raise ValueError("Answer options must not repeat.")
        if not isinstance(answers, list) or len(answers) not in (1, 2):
            raise ValueError("Each question needs one or two correct answers.")
        for answer in answers:
            if not isinstance(answer, str) or answer not in options:
                raise ValueError("Correct answers must be among the options.")
        if len(set(answers)) != len(answers) or not isinstance(item.get("fact"), str):
            raise ValueError("Check the question's answers and fact.")
    return questions

# Load the scores from previous games.
def load_scores():
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r", encoding="utf-8") as file:
        scores = json.load(file)
    if not isinstance(scores, list):
        raise ValueError("Scores.json must be a list of results. The supplied file starts with [].")
    text_fields = ["quiz_id", "user_id", "name", "mode", "reason", "date"]
    number_fields = ["score", "max_score", "correct", "incorrect", "unanswered", "seconds"]
    for record in scores:
        if not isinstance(record, dict):
            raise ValueError("Scores.json contains an invalid result.")
        for field in text_fields:
            if not isinstance(record.get(field), str):
                raise ValueError("Scores.json has missing or invalid text fields.")
        for field in number_fields:
            if not isinstance(record.get(field), (int, float)):
                raise ValueError("Scores.json has missing or invalid numeric fields.")
    return scores


# Work out the final results.
def make_summary():
    correct = 0
    incorrect = 0
    for points in session["question_scores"].values():
        if points > 0:
            correct += 1
        else:
            incorrect += 1
    total = len(session["selected_questions"])
    unanswered = total - correct - incorrect
    total_time = session["end_time"] - session["start_time"]
    total_time = round(total_time, 2)

    # Turn the finish time into text for the history table.
    finish_time = time.gmtime(session["end_time"])
    date_text = time.strftime("%Y-%m-%d %H:%M UTC", finish_time)

    summary = {
        "quiz_id": session["quiz_id"],
        "user_id": session["user_id"],
        "name": session["name"],
        "score": session["score"],
        "max_score": total * 15,
        "correct": correct,
        "incorrect": incorrect,
        "unanswered": unanswered,
        "seconds": total_time,
        "mode": session["mode"],
        "reason": session["reason"],
        "date": date_text
    }
    return summary

# ChatGPT helped save each result once and fix the file path handling.
def save_score():
    # The quiz ID prevents refreshes/API retries from saving a result twice.
    scores = load_scores()
    for record in scores:
        if record["quiz_id"] == session["quiz_id"]:
            return False
    scores.append(make_summary())
    temporary_file = str(SCORES_FILE) + ".tmp"
    with open(temporary_file, "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=4, ensure_ascii=False)
    os.replace(temporary_file, SCORES_FILE)
    return True

# Scoring and timing
def calculate_points(user_answers, correct_answers, seconds):
    points = 0
    if set(user_answers) == set(correct_answers):
        points = 10
        if seconds <= SPEED_BONUS_LIMIT:
            points += 5
    return points

# End the quiz and save the result.
def finish_quiz(reason):
    if not session.get("finished"):
        session["finished"] = True
        session["reason"] = reason
        session["end_time"] = time.time()
        if reason == "timeout":
            session["end_time"] = session["question_start"] + QUESTION_TIME_LIMIT
    save_score()

# Check if this question has run out of time.
# ChatGPT helped check the deadline in Python for requirement 3.
def time_is_up():
    if not session.get("quiz_id"):
        return False
    if session.get("finished"):
        return False
    if session["mode"] == "practice":
        return False
    question_key = str(session["current_question"])
    if question_key in session["question_scores"]:
        return False  # The player is reading the feedback.

    time_used = time.time() - session["question_start"]
    if time_used >= QUESTION_TIME_LIMIT:
        return True
    return False

# Show the home page and remember the player's name.
# ChatGPT helped use sessions for returning players and their history (requirement 1).
@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        name = request.form.get("name", "").strip()
        if name == "" or len(name) > 30 or not name.isprintable():
            message = "Please enter a name with 1 to 30 printable characters."
        else:
            session["name"] = name
            if "user_id" not in session:
                session["user_id"] = secrets.token_hex(16)
            session.permanent = True
            return redirect('/')
    history = []
    best_score = 0
    if "user_id" in session:
        for record in load_scores():
            if record["user_id"] == session["user_id"]:
                history.append(record)
                if record["score"] > best_score:
                    best_score = record["score"]
    history.reverse()
    return render_template(
        'index.html',
        history=history,
        best_score=best_score,
        message=message,
        time_limit=QUESTION_TIME_LIMIT
    )



# Pick the questions and start a new game.
@app.route('/start', methods=['POST'])
def start():
    if "name" not in session:
        return redirect('/')
    mode = request.form.get("mode", "challenge")
    if mode not in ("challenge", "practice"):
        return render_template('error.html', message="Please choose a valid quiz mode."), 400
    questions = load_questions()
    session["selected_questions"] = random.sample(list(questions.keys()), NUM_QUESTIONS_PER_QUIZ)
    shuffled_options = {}
    for question in session["selected_questions"]:
        options = questions[question]["options"].copy()
        random.shuffle(options)
        shuffled_options[question] = options
    session["shuffled_options"] = shuffled_options
    session["score"] = 0
    session["question_scores"] = {}
    session["user_answers"] = {}
    session["answer_times"] = {}
    session["current_question"] = 0
    session["quiz_id"] = secrets.token_hex(16)
    session["mode"] = mode
    session["start_time"] = time.time()
    session["question_start"] = time.time()
    session["finished"] = False
    return redirect('/quiz')


# Show the question and check the player's answer.
# ChatGPT helped with answer validation and stopping repeated scoring.
@app.route('/quiz', methods=['GET', 'POST'])
@app.route('/quiz/<int:question_number>', methods=['GET', 'POST'])
def quiz(question_number=0):
    question_list = session.get("selected_questions")
    if not question_list:
        return redirect('/')
    if session.get("finished"):
        return redirect('/result')
    if time_is_up():
        finish_quiz("timeout")
        return redirect('/result')
    if question_number != session["current_question"]:
        return redirect('/quiz/' + str(session["current_question"]))
    questions = load_questions()
    question = question_list[question_number]
    if question not in questions:
        raise ValueError("The question file changed. Go home and start a new quiz.")
    options = session["shuffled_options"][question]
    correct_answers = questions[question]["answers"]
    answer_count = len(correct_answers)
    question_key = str(question_number)
    question_scores = session["question_scores"]
    message = ""

    if request.method == 'POST' and question_key not in question_scores:
        user_answers = request.form.getlist("answer")
        valid = True
        if len(user_answers) != answer_count:
            valid = False
        for answer in user_answers:
            if answer not in options:
                valid = False
            if user_answers.count(answer) > 1:
                valid = False
        if not valid:
            message = "Please choose exactly " + str(answer_count) + " different answer(s)."
        else:
            seconds = time.time() - session["question_start"]
            if session["mode"] == "challenge" and seconds >= QUESTION_TIME_LIMIT:
                finish_quiz("timeout")
                return redirect('/result')
            points = calculate_points(user_answers, correct_answers, seconds)
            question_scores[question_key] = points
            session["question_scores"] = question_scores

   # Add up the points from all answered questions.
            total_score = 0
            for question_points in question_scores.values():
                total_score += question_points
            session["score"] = total_score

    # Keep the answers for the review page.
            all_answers = session["user_answers"]
            all_answers[question_key] = user_answers
            session["user_answers"] = all_answers
            answer_times = session["answer_times"]
            answer_times[question_key] = round(seconds, 2)
            session["answer_times"] = answer_times
            if len(question_scores) == len(question_list):
                finish_quiz("completed")
                return redirect('/result')
            return redirect('/quiz/' + str(question_number))
    
    answered = False
    if question_key in question_scores:
        answered = True
    points = question_scores.get(question_key, 0)
    fact = ""
    if answered:
        if points > 0:
            message = "Correct!"
        else:
            message = "Incorrect! Correct answers: " + ", ".join(correct_answers)
        fact = questions[question]["fact"]
    time_used = time.time() - session["question_start"]
    remaining = QUESTION_TIME_LIMIT - time_used
    if remaining < 0:
        remaining = 0
    selected = session["user_answers"].get(question_key, [])

    return render_template(
        'quiz.html',
        question=question,
        options=options,
        message=message,
        answer_count=answer_count,
        question_number=question_number,
        total_questions=len(question_list),
        fact=fact,
        points=points,
        answered=answered,
        remaining=remaining,
        selected=selected
    )


# Move to the next question after an answer is submitted.
@app.route('/next', methods=['POST'])
def next_question():
    if not session.get("quiz_id"):
        return redirect('/')
    if session.get("finished"):
        return redirect('/result')
    if time_is_up():
        finish_quiz("timeout")
        return redirect('/result')
    current = session["current_question"]
    if str(current) in session["question_scores"]:
        session["current_question"] = current + 1
        session["question_start"] = time.time()
    return redirect('/quiz/' + str(session["current_question"]))


# Show the final score and the answers to review.
# ChatGPT helped build the final summary and question review.
@app.route('/result')
def result():
    if not session.get("quiz_id"):
        return redirect('/')
    if time_is_up():
        finish_quiz("timeout")
    if not session.get("finished"):
        return redirect('/quiz/' + str(session["current_question"]))
    save_score() # Try again if the previous save did not work.
    questions = load_questions()
    review = []
    number = 0
    for question in session["selected_questions"]:
        if question not in questions:
            raise ValueError("The question file changed. Restore it to show this review.")
        key = str(number)
        status = "Not answered"
        if key in session["question_scores"]:
            if session["question_scores"][key] > 0:
                status = "Correct"
            else:
                status = "Incorrect"
        item = {
            "question": question,
            "status": status,
            "chosen": session["user_answers"].get(key, []),
            "answers": questions[question]["answers"],
            "fact": questions[question]["fact"],
            "points": session["question_scores"].get(key, 0)
        }
        review.append(item)
        number += 1
    return render_template('result.html', summary=make_summary(), review=review)




# Send the current question as JSON for the API requirement.
# ChatGPT helped create both APIs below for questions and saved scores.
@app.route('/api/questions', methods=['GET'])
def api_questions():
    if not session.get("quiz_id"):
        return jsonify(error="Start a quiz first."), 409
    if time_is_up():
        finish_quiz("timeout")
    if session.get("finished"):
        return jsonify(error="This quiz has finished."), 409
    question_list = session["selected_questions"]
    question_number = session["current_question"]
    question = question_list[question_number]
    questions = load_questions()
    if question not in questions:
        raise ValueError("The question file changed. Start a new quiz.")
    question_data = {
        "question": question,
        "options": session["shuffled_options"][question],
        "answer_count": len(questions[question]["answers"]),
        "question_number": question_number,
        "total": NUM_QUESTIONS_PER_QUIZ
    }
    return jsonify(question_data)

# Get this player's past scores or save the finished quiz.
@app.route('/api/scores', methods=['GET', 'POST'])
def api_scores():
    if "user_id" not in session:
        return jsonify(error="Enter your name first."), 401
    if request.method == 'POST':
        if not session.get("finished"):
            return jsonify(error="Finish the quiz first."), 409
        created = save_score()
        status_code = 200
        if created:
            status_code = 201
        return jsonify(saved=True, result=make_summary(), already_saved=not created), status_code
    history = []
    for record in load_scores():
        if record["user_id"] == session["user_id"]:
            history.append(record)
    return jsonify(scores=history)


# Show a helpful message if a data file cannot be read or saved.
@app.errorhandler(ValueError)
@app.errorhandler(OSError)
def data_error(error):
    message = "Cannot read or save the quiz data. Check Question.json, Scores.json and folder permissions. " + str(error)
    if request.path.startswith('/api/'):
        return jsonify(error=message), 503
    return render_template('error.html', message=message), 503


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', message="The requested page does not exist. Please return home."), 404


@app.after_request
def avoid_old_pages(response):
    # Ask the browser to load the current page again instead of an old copy.
    response.headers["Cache-Control"] = "no-store"
    return response


if __name__ == '__main__':
    app.run(debug=False, port=5001, threaded=False)
