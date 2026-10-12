import json
import random
import time

# Load questions from JSON file
with open("Question.json", "r") as file:
    questions = json.load(file)


NUM_QUESTIONS_PER_QUIZ = 5
# Load previous high scores
with open("Scores.json", "r") as file:
    high_scores = json.load(file)

#Get a valid answer from the user
def get_answer(options, letters, message):
    answer = input(message).strip().lower()

    # Keep prompting the user until a valid answer is provided
    while answer == "" or answer not in letters[:len(options)]:
        print("Invalid answer! Please try again.")
        answer = input(message).strip().lower()
    #convert the letter answer to the corresponding option
    answer_index = letters.index(answer)
    return options[answer_index]

#welcome message 
print("welcome to the cat knowledge quiz!")
print("Let's see how much you know about cats!")
username = input("Enter your name: ")
while username.strip() == "":
    print("Name cannot be empty. Please enter your name.")
    username = input("Enter your name: ")
print("Welcome,", username + "!")

#explain the scoring system to the user
print("Each correct answer is worth 10 points.")
print("Answer within 5 seconds to earn 5 bonus points!")
time.sleep(1)

#randomly select questions for the quiz
selected_questions = random.sample(list(questions.keys()), NUM_QUESTIONS_PER_QUIZ)
score = 0
question_number = 0

# Loop through each selected question and present it to the user
for question in selected_questions:
    question_number += 1
    print("\nQuestion", question_number, "of", NUM_QUESTIONS_PER_QUIZ)
    print(question)

    letters = "abcdef"
    options = questions[question]["options"]

    #Display the answer options with letters
    for i in range(len(options)):
        print(letters[i] + ". " + options[i])

    correct_answers = questions[question]["answers"]
    #Start the timer for this question
    start_time = time.time()
    is_correct = False
    #For questions with a single correct answer
    if len(correct_answers) == 1:
        user_answer1 = get_answer(options, letters, "Enter your answer: ")

        if user_answer1 == correct_answers[0]:
            print("Correct!")
            is_correct = True
        else:
            print("Incorrect!")
            print("Correct answer:", correct_answers[0])

    #For questions with two correct answers
    elif len(correct_answers) == 2:
        user_answer1 = get_answer(options, letters, "Enter your first answer: ")
        user_answer2 = get_answer(options, letters, "Enter your second answer: ")

        while user_answer2 == user_answer1:
            print("You cannot choose the same answer twice!")
            user_answer2 = get_answer(options, letters, "Enter your second answer: ")

        if user_answer1 in correct_answers and user_answer2 in correct_answers:
            print("Correct!")
            is_correct = True
        else:
            print("Incorrect!")
            print("Correct answers:", ", ".join(correct_answers))
    

    #calculate the time taken and update the score based on correctness and speed
    end_time = time.time()
    answer_time = end_time - start_time

    if not is_correct:
            print("Cat Fun Fact:", questions[question]["fact"])
    
    print("Time taken for this question: {:.2f} seconds".format(answer_time))
    if is_correct:
        score += 10
        if answer_time <= 5:
            score += 5
            print("Speed bonus! + 5 points")

#Display the final results
print("\nQuiz Completed!")
print("Your final score is:", score, "out of 75")
if username not in high_scores:
    high_scores[username] = score

elif score > high_scores[username]:
    high_scores[username] = score

print("Your personal best:", high_scores[username])

#give user feedback based on their final score
print("Thank you for playing the cat knowledge quiz!")
if score >= 60:
    print("You're a Cat Expert! ")
elif score >= 35:
    print("You're a Cat Lover!")
else:
    print("Keep learning about cats!")
# Find the player with the highest score
champion = max(high_scores, key=high_scores.get)

print("\n=== Leaderboard ===")

for player in high_scores:
    print(player, "-", high_scores[player], "points")

print("\nGrand Champion:", champion)
print("Champion's Score:", high_scores[champion])

# Save high scores to the JSON file
with open("Scores.json", "w") as file:
    json.dump(high_scores, file, indent=4)

