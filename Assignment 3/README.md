This project turns my Assignment 1 Cat Quiz into a Flask web application.
Players answer five random cat questions and view their results and history.

My individual requirements are 
1: Persistent User Identification and History
and 
3: Timer-Based Challenge Mode.


How to Run

1. Open the project folder in VS Code. Keep Question.json, templates and
   static beside webapp_quiz.py.
2. Open a terminal in that folder and install Flask
3. Start the app:
   python3 webapp_quiz.py
4. Open http://127.0.0.1:5001/.


How to Play
1. Enter your name on the home page.
2. Choose Challenge or Practice and click Start Quiz.
3. Select the required number of answers and click Submit Answer.
4. Read the feedback and cat fact, then click Next Question.
5. After five questions, view your results. Return Home to see your saved history.
Challenge allows 20 seconds per question. When time runs out, the whole quiz ends.
The timer pauses on feedback and starts again for the next question. Refreshing
does not restart it. Practice has no deadline.

Scoring and Results
- Correct answer: 10 points.
- Correct within 5 seconds: 5 extra points.
- Wrong answer: 0 points.
- Two-answer questions require both correct choices.
- Maximum score: 75 points in either mode.
Results show the score, correct, incorrect and unanswered counts, total time, and questions to review.
Total time includes reading feedback between questions.


Design Choices
Flask handles pages and submitted answers. HTML templates display the data,
CSS styles the pages, and JavaScript updates the countdown. JSON keeps the small question bank and history easy to read and update.

Sessions remember the player and current game. The browser can recognize a
returning player for 30 days while its cookie is retained. The app automatically
creates secret_key.txt; keep it between runs so existing sessions still work.

Use of AI
ChatGPT helped with parts of the app, debugging, tests and documentation,
including this README. Details are in UseOfAI.md.

