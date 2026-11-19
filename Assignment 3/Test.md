# Test record
I used ChatGPT to help generate automated tests for my quiz. The test code is in test_quiz.py.

ChatGPT ran all 36 automated tests in its testing environment using Python 3.12.14 and Flask 3.1.3. All tests passed with the uploaded Python code and the prepared HTML, CSS and JavaScript files.

The tests use temporary question and score files, so they do not change the original questions or saved history. A controlled clock checks the time limits without waiting 20 real seconds.

I also ran the scoring test on my computer. It completed successfully with “Ran 1 test” and “OK.”

Command to run all automated tests:  python3 -m unittest -v test_quiz.py


Test includes:
# Scoring  
Correct answers earn 10 points. Correct answers within 5 seconds earn 15 points. Wrong answers earn 0 points.
# Multiple answers 
Both correct answers must be selected. Their order does not matter.
# Input validation 
Blank names, invalid names and incorrect answer selections are rejected.
# Randomization
Questions and options are shuffled when a game starts. Refreshing preserves the current game's order.
# Quiz navigation 
Players cannot skip unanswered questions or use an old question page to answer the next question.
# Repeated submissions 
Submitting the same answer again does not add extra points.
# Timer
Challenge ends at the deadline. Refreshing does not restart the timer. Practice has no deadline.
# Results  
Final score, correct/incorrect counts, unanswered questions and answer review are checked.
# History 
Results are saved once. Returning visitors can access their own history.
# APIs
Question and score endpoints return the expected data. Submitted score values cannot replace the calculated score.
# File errors  
Missing or invalid question data and empty or corrupt score files show helpful errors.
# Static files
style.css and timer.js can be loaded, and the quiz page includes the countdown elements.



# Browser acceptance checklist
I tested the quiz in my browser, and all the checks passed. The app remembered my name and history after I closed and reopened the browser and after I restarted the Python server while keeping secret_key.txt. Practice mode showed five questions and displayed the final score, answer counts, total time and answer review. Invalid answer selections showed a helpful message without advancing, and repeated submissions did not add extra points. In Challenge mode, the countdown decreased correctly, and the quiz ended automatically and saved the result when time reached zero. Refreshing after about eight seconds left about twelve seconds instead of restarting the timer. Feedback stayed available until I clicked Next, and the next question received a new timer. Refreshing the results page did not create duplicate history entries. The /api/questions and /api/scores endpoints displayed the expected JSON data. Finally, the page remained usable in a narrow window, and I could navigate the controls using Tab with visible keyboard focus.