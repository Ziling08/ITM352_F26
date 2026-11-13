# Cat Knowledge Quiz — Flask

1. Unzip the folder and open it in VS Code.
2. Open a terminal in Cat_Quiz_Flask.
3. Run `python3 -m pip install -r requirements.txt`.
4. Run `python3 app.py`.
5. Open http://127.0.0.1:5000 in your browser.

On Windows, use `python` if `python3` is unavailable. Stop with Ctrl+C.

app.py contains the Python game logic. templates contains the HTML pages.
Question.json contains your existing question bank and answer keys, preserved as supplied.
Scores.json starts empty and saves personal best scores between runs.
You may copy your old Scores.json here before starting to retain your old scores.

The game keeps five random questions, single/two-answer questions, 10-point
correct answers, a 5-point speed bonus, wrong-answer facts, and a leaderboard.
The timer includes page loading and submission time and does not reset on refresh
or invalid answers. A separate feedback page lets you read before starting the next timer.

This is a beginner-friendly local classroom app. Active games reset when the
server restarts; high scores remain saved. Names identify players (no accounts).
Use one local server process. A public deployment would need persistent server
sessions, a database, and additional security. The original question bank includes
some potentially ambiguous choices; review the answer keys before grading.

AI assistance: ChatGPT converted the supplied console quiz into Flask routes and
HTML templates and tested the quiz flow, answer validation, scoring, and saving.
