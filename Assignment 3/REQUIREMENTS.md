# Assignment 3 Requirements

## Core Requirements

1. # User Interface
   HTML templates show the home page, quiz and results. CSS styles the pages, and JavaScript updates the countdown.

2. # Question Display
   Questions and choices are loaded from Question.json. Each game randomly selects five questions and shuffles the answer choices.

3. # Answer Submission and Feedback
   Players submit their answers using a form. The quiz shows whether the answer is correct and gives the correct answers when needed. A correct answer earns 10 points, with 5 extra points for answering within 5 seconds.

4. # Data Management
   Questions are stored in Question.json, and completed results are stored in Scores.json. Python reads and saves these files.

5. # Backend and APIs
   Flask runs the app. GET /api/questions returns the current question, GET /api/scores returns the player's history, and POST /api/scores saves a completed result.

6. # Score Tracking and Detailed Feedback
   The results page shows the final score, correct and incorrect counts, unanswered questions and total time. It also shows the correct answers, cat facts and questions to review.

7. # Error Handling and Validation
   The name form checks for blank or invalid names. The quiz checks the number of selected answers and rejects invalid choices. File errors show a readable message. Player identification uses a name and session.

8. # User-Friendliness
   The pages have clear instructions, labeled choices and simple navigation buttons. CSS adjusts the layout for smaller screens.

9. # Documentation
   README.md explains setup, usage and design choices. Code comments explain the main steps. UseOfAI.md describes AI assistance, and this file explains how the requirements are addressed.

10. # Performance
    Each game uses five questions from a small JSON file. CSS and JavaScript are stored locally, and the pages do not use large images or extra front-end frameworks.

11. # Quality Assurance
    test_quiz.py includes unit and integration tests for scoring, routes, timing, validation and saved results. Test.md includes a checklist for testing the app in a browser.

12. # Maintainability
    Functions such as load_questions(), calculate_points() and save_score() separate the main tasks. Python, HTML, CSS, JavaScript and JSON are kept in separate files.

## Individual Requirements

1. # Persistent User Identification and History 
Flask sessions remember the player's name and user ID. The home page welcomes returning players and shows their saved score history and personal best.

3. # Timer-Based Challenge Mode**
Challenge mode gives the player 20 seconds per question. The page displays a countdown, and the whole quiz ends when time reaches zero. Python also checks the time limit, and refreshing the page does not restart the timer.