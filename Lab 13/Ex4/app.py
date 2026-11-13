import json
import random
import secrets
import time
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
BASE_DIR = Path(__file__).resolve().parent
SCORES_FILE = BASE_DIR / 'Scores.json'
with open(BASE_DIR / 'Question.json', encoding='utf-8') as file:
    questions = json.load(file)

NUM_QUESTIONS_PER_QUIZ = 5
# Store active games on the server, so answers and scores stay out of cookies.
games = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        if not username or len(username) > 50:
            error = 'Please enter a name between 1 and 50 characters.'
        else:
            games.pop(session.get('game_id'), None)
            session.clear()
            game_id = secrets.token_hex(16)
            session['game_id'] = game_id
            games[game_id] = {
                'username': username,
                'selected': random.sample(list(questions), NUM_QUESTIONS_PER_QUIZ),
                'number': 0, 'score': 0, 'started': None,
                'feedback': None, 'saved': False
            }
            return redirect(url_for('quiz'))
    return render_template('index.html', error=error)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    game = games.get(session.get('game_id'))
    if game is None:
        return redirect(url_for('index'))
    if game['number'] >= NUM_QUESTIONS_PER_QUIZ:
        return redirect(url_for('result'))
    if game['feedback'] is not None:
        return redirect(url_for('feedback'))

    question = game['selected'][game['number']]
    data = questions[question]
    error = None
    if game['started'] is None:
        game['started'] = time.monotonic()
    if request.method == 'POST':
        answers = request.form.getlist('answer')
        # Check the question number to prevent an old form scoring a new question.
        if request.form.get('number') != str(game['number']):
            return redirect(url_for('quiz'))
        if (len(answers) != len(data['answers']) or
                len(set(answers)) != len(answers) or
                any(answer not in data['options'] for answer in answers)):
            error = 'Choose exactly ' + str(len(data['answers'])) + ' different answer(s).'
        else:
            elapsed = time.monotonic() - game['started']
            correct = set(answers) == set(data['answers'])
            points = 10 if correct else 0
            bonus = correct and elapsed <= 5
            if bonus:
                points += 5
            game['score'] += points
            game['feedback'] = {
                'correct': correct, 'answers': data['answers'], 'fact': data['fact'],
                'elapsed': round(elapsed, 2), 'points': points, 'bonus': bonus
            }
            return redirect(url_for('feedback'))
    return render_template('quiz.html', game=game, question=question,
                           data=data, error=error)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    game = games.get(session.get('game_id'))
    if game is None:
        return redirect(url_for('index'))
    if game['feedback'] is None:
        return redirect(url_for('quiz'))
    if request.method == 'POST':
        if request.form.get('number') != str(game['number']):
            return redirect(url_for('feedback'))
        game['number'] += 1
        game['started'] = None
        game['feedback'] = None
        return redirect(url_for('quiz'))
    return render_template('feedback.html', game=game, feedback=game['feedback'])


@app.route('/result')
def result():
    game = games.get(session.get('game_id'))
    if game is None:
        return redirect(url_for('index'))
    if game['number'] < NUM_QUESTIONS_PER_QUIZ:
        return redirect(url_for('quiz'))
    if SCORES_FILE.exists():
        with open(SCORES_FILE, encoding='utf-8') as file:
            high_scores = json.load(file)
    else:
        high_scores = {}
    if not game['saved']:
        name = game['username']
        high_scores[name] = max(game['score'], high_scores.get(name, 0))
        with open(SCORES_FILE, 'w', encoding='utf-8') as file:
            json.dump(high_scores, file, indent=4)
        game['saved'] = True
    leaderboard = sorted(high_scores.items(), key=lambda item: item[1], reverse=True)
    if game['score'] >= 60:
        message = "You're a Cat Expert!"
    elif game['score'] >= 35:
        message = "You're a Cat Lover!"
    else:
        message = 'Keep learning about cats!'
    return render_template('result.html', game=game, message=message,
                           best=high_scores[game['username']], leaderboard=leaderboard)


if __name__ == '__main__':
    # Local classroom app; one request at a time keeps JSON score writes simple.
    app.run(port=5000, threaded=False)
