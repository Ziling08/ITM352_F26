

I used ChatGPT to  generate and revise parts of the Python code, HTML templates, CSS and JavaScript.

For individual requirement 1, ChatGPT helped use Flask sessions to remember the player’s name and user ID. It helped save completed results in Scores.json and display the returning player’s history and personal best on the home page.

For individual requirement 3, ChatGPT helped create a 20-second countdown for each question in Challenge mode. JavaScript updates the visible timer, while Python checks whether the time limit has been reached. The quiz ends when time runs out, and refreshing the page does not restart the timer.

ChatGPT also helped create the required APIs: GET /api/questions, GET /api/scores and POST /api/scores. These return question data, show the player’s history and save a completed result.

# Finding and fixing bugs

ChatGPT reviewed the code I uploaded and helped identify specific problems:
- I had written options = item.get and answers = item.get without calling the method. It showed me how to use item.get("options") and item.get("answers").
- An empty Scores.json caused the error “Expecting value: line 1 column 1.” It explained that an empty score history should contain [].
- The browser could not find style.css, and the timer displayed .... It helped me check the static folder, the JavaScript link and the countdown elements in quiz.html.

# Generating tests

ChatGPT generated and adjusted the 36 automated tests in test_quiz.py. They check scoring, answer selection, navigation, sessions, timing, history, APIs and file errors.
The tests use temporary files to protect the original data and a controlled clock to test time limits. I ran the scoring test in my Terminal and received “OK.” I also used the browser checklist to test the app’s behavior.

ChatGPT also helped write the requirements explanation, testing documentation and this AI-use explanation.”