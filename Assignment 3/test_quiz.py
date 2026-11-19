# Tests for my Cat Quiz. ChatGPT helped write and adjust this file.
# Start with the scoring test, then run all tests.
# Run all: python3 -m unittest -v test_quiz.py
# Question and score files used by the tests are temporary copies.
import json
import os
import shutil
import tempfile
import unittest
from unittest.mock import patch

import webapp_quiz as quiz


# Read and write only the temporary test files.
def read_text(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_text(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


class QuizTests(unittest.TestCase):
    def setUp(self):
        # Each test starts with its own files and browser session.
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        original_questions = quiz.QUESTIONS_FILE
        original_scores = quiz.SCORES_FILE
        self.addCleanup(setattr, quiz, "QUESTIONS_FILE", original_questions)
        self.addCleanup(setattr, quiz, "SCORES_FILE", original_scores)
        quiz.QUESTIONS_FILE = os.path.join(self.folder.name, "Question.json")
        quiz.SCORES_FILE = os.path.join(self.folder.name, "Scores.json")
        shutil.copyfile(original_questions, quiz.QUESTIONS_FILE)
        self.addCleanup(quiz.app.config.update, TESTING=quiz.app.config["TESTING"])
        quiz.app.config["TESTING"] = True
        self.client = quiz.app.test_client()
        # Control the time so the tests do not have to wait 20 seconds.
        clock_patch = patch("webapp_quiz.time.time", return_value=1000.0)
        self.clock = clock_patch.start()
        self.addCleanup(clock_patch.stop)

    def register(self, name="Cat Student", client=None):
        client = client or self.client
        return client.post('/', data={"name": name}, follow_redirects=True)

    def start(self, mode="practice"):
        self.register()
        return self.client.post('/start', data={"mode": mode}, follow_redirects=True)

    def state(self):
        # Look at the current game's saved session values.
        with self.client.session_transaction() as session:
            return dict(session)

    def current_answers(self):
        state = self.state()
        question = state["selected_questions"][state["current_question"]]
        return quiz.load_questions()[question]["answers"]

    def wrong_answers(self):
        state = self.state()
        question = state["selected_questions"][state["current_question"]]
        item = quiz.load_questions()[question]
        answers = item["answers"].copy()
        for option in item["options"]:
            if option not in item["answers"]:
                answers[0] = option
                return answers
        self.fail("This question needs at least one wrong option for this test.")

    def answer(self, answers=None):
        if answers is None:
            answers = self.current_answers()
        number = self.state()["current_question"]
        return self.client.post('/quiz/' + str(number), data={"answer": answers}, follow_redirects=True)

    def finish(self):
        self.start()
        for number in range(5):
            response = self.answer()
            if number < 4:
                self.client.post('/next', follow_redirects=True)
        return response

    def test_points_and_speed_bonus(self):
        # At 5 seconds: 15 points. After 5 seconds: 10 points. Wrong: 0.
        self.assertEqual(quiz.calculate_points(["A"], ["A"], 5), 15)
        self.assertEqual(quiz.calculate_points(["A"], ["A"], 5.01), 10)
        self.assertEqual(quiz.calculate_points(["B"], ["A"], 2), 0)

    def test_two_answers_exact_set_and_order(self):
        self.assertEqual(quiz.calculate_points(["B", "A"], ["A", "B"], 2), 15)
        self.assertEqual(quiz.calculate_points(["A", "C"], ["A", "B"], 2), 0)

    def test_name_validation(self):
        for name in ("   ", "a" * 31, "bad\nname"):
            response = self.register(name)
            self.assertIn(b"Please enter a name", response.data)
            self.assertNotIn("name", self.state())

    def test_visitor_cookie_is_persistent_and_name_is_escaped(self):
        response = self.register("<script>Mimi</script>")
        self.assertNotIn(b"<script>Mimi</script>", response.data)
        self.assertIn(b"&lt;script&gt;Mimi", response.data)
        self.assertTrue(self.state()["_permanent"])
        self.assertIsNotNone(self.client.get_cookie("session").expires)

    def test_new_browser_with_saved_cookie_recognizes_visitor(self):
        self.finish()
        other = quiz.app.test_client()
        other.set_cookie("session", self.client.get_cookie("session").value)
        response = other.get('/')
        self.assertIn(b"Welcome back, Cat Student!", response.data)
        self.assertEqual(len(other.get('/api/scores').json["scores"]), 1)

    def test_same_names_have_separate_histories(self):
        self.finish()
        other = quiz.app.test_client()
        self.register("Cat Student", client=other)
        self.assertEqual(other.get('/api/scores').json["scores"], [])

    def test_invalid_mode(self):
        self.register()
        response = self.client.post('/start', data={"mode": "fake"})
        self.assertEqual(response.status_code, 400)

    def test_randomization_is_preserved_across_requests(self):
        self.register()
        original = read_text(quiz.QUESTIONS_FILE)
        source = json.loads(original)
        expected_questions = list(source.keys())
        expected_questions.reverse()
        expected_questions = expected_questions[:5]

        # Make random choices predictable so this test is repeatable.
        def reverse_options(options):
            options.reverse()

        with patch("webapp_quiz.random.sample", return_value=expected_questions) as sample_mock:
            with patch("webapp_quiz.random.shuffle", side_effect=reverse_options) as shuffle_mock:
                self.client.post('/start', data={"mode": "practice"}, follow_redirects=True)
        sample_mock.assert_called_once_with(list(source.keys()), 5)
        self.assertEqual(shuffle_mock.call_count, 5)
        state = self.state()
        self.assertEqual(state["selected_questions"], expected_questions)
        for question in state["selected_questions"]:
            expected_options = source[question]["options"].copy()
            expected_options.reverse()
            self.assertEqual(state["shuffled_options"][question], expected_options)
        self.client.get('/quiz')
        self.assertEqual(self.state()["selected_questions"], state["selected_questions"])
        self.assertEqual(self.state()["shuffled_options"], state["shuffled_options"])
        self.assertEqual(read_text(quiz.QUESTIONS_FILE), original)

    def test_invalid_answers_do_not_score_or_advance(self):
        self.start()
        for answers in ([], ["fake"], ["fake", "fake"]):
            self.answer(answers)
            self.assertEqual(self.state()["score"], 0)
            self.assertEqual(self.state()["question_scores"], {})
        self.client.post('/next', follow_redirects=True)
        self.assertEqual(self.state()["current_question"], 0)

    def test_wrong_answer_shows_correct_answer_and_fact(self):
        self.start()
        response = self.answer(self.wrong_answers())
        self.assertIn(b"Incorrect! Correct answers:", response.data)
        self.assertIn(b"Cat Fun Fact:", response.data)
        self.assertEqual(self.state()["question_scores"]["0"], 0)

    def test_same_question_cannot_be_scored_twice(self):
        self.start()
        self.answer()
        self.answer()
        self.assertEqual(self.state()["score"], 15)
        self.assertEqual(len(self.state()["question_scores"]), 1)

    def test_first_answer_stays_locked(self):
        self.start()
        original = self.current_answers()
        self.answer(original)
        self.answer(["a different answer"])
        self.assertEqual(self.state()["user_answers"]["0"], original)
        self.assertEqual(self.state()["score"], 15)

    def test_question_url_cannot_skip_questions(self):
        self.start()
        self.client.get('/quiz/4', follow_redirects=True)
        self.assertEqual(self.state()["current_question"], 0)
        self.client.get('/result', follow_redirects=True)
        self.assertFalse(self.state()["finished"])

    def test_old_form_does_not_answer_next_question(self):
        self.start()
        self.answer()
        self.client.post('/next', follow_redirects=True)
        self.client.post('/quiz/0', data={"answer": self.current_answers()}, follow_redirects=True)
        self.assertEqual(len(self.state()["question_scores"]), 1)

    def test_home_does_not_reset_current_game(self):
        self.start()
        self.answer()
        game_id = self.state()["quiz_id"]
        self.client.get('/')
        self.assertEqual(self.state()["score"], 15)
        self.assertEqual(self.state()["quiz_id"], game_id)

    def test_new_game_resets_score_not_name_or_history(self):
        self.finish()
        self.client.post('/start', data={"mode": "challenge"}, follow_redirects=True)
        self.assertEqual(self.state()["score"], 0)
        self.assertEqual(self.state()["name"], "Cat Student")
        self.assertEqual(len(self.client.get('/api/scores').json["scores"]), 1)

    def test_refresh_does_not_restart_timer(self):
        self.start("challenge")
        self.clock.return_value = 1008
        self.client.get('/quiz')
        self.assertEqual(self.state()["question_start"], 1000)

    def test_deadline_rejects_late_answer_and_ends_whole_quiz(self):
        self.start("challenge")
        self.clock.return_value = 1020
        response = self.answer()
        self.assertIn(b"Time's up!", response.data)
        record = quiz.load_scores()[0]
        self.assertEqual(record["score"], 0)
        self.assertEqual(record["unanswered"], 5)
        self.assertEqual(record["seconds"], 20)
        self.assertEqual(record["reason"], "timeout")

    def test_timeout_is_checked_on_return_without_javascript(self):
        self.start("challenge")
        self.clock.return_value = 1500
        self.client.get('/quiz', follow_redirects=True)
        self.assertTrue(self.state()["finished"])
        self.assertEqual(quiz.load_scores()[0]["seconds"], 20)

    def test_feedback_pauses_timer_until_next_question(self):
        self.start("challenge")
        self.clock.return_value = 1004
        self.answer()
        self.clock.return_value = 1100
        self.client.get('/quiz')
        self.assertFalse(self.state()["finished"])
        self.client.post('/next', follow_redirects=True)
        self.assertEqual(self.state()["question_start"], 1100)

    def test_practice_has_no_deadline(self):
        self.start()
        self.clock.return_value = 2000
        self.answer()
        self.assertEqual(self.state()["score"], 10)
        self.assertFalse(self.state()["finished"])

    def test_summary_history_and_save_once(self):
        response = self.finish()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"75 / 75", response.data)
        self.assertIn(b"Correct: 5", response.data)
        self.assertIn(b"Question Review", response.data)
        self.client.get('/result')
        self.client.get('/result')
        self.assertEqual(len(quiz.load_scores()), 1)
        self.assertLess(len(self.client.get_cookie("session").value), 3800)

    def test_api_questions_omits_answer_key_and_fact(self):
        self.start()
        response = self.client.get('/api/questions')
        self.assertEqual(response.status_code, 200)
        self.assertIn("options", response.json)
        self.assertNotIn("answers", response.json)
        self.assertNotIn("fact", response.json)

    def test_api_scores_ignores_supplied_score_and_prevents_duplicates(self):
        self.finish()
        response = self.client.post('/api/scores', json={"score": 999999})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"]["score"], 75)
        self.assertTrue(response.json["already_saved"])
        self.assertEqual(len(quiz.load_scores()), 1)

    def test_api_state_validation(self):
        self.assertEqual(self.client.get('/api/scores').status_code, 401)
        self.assertEqual(self.client.get('/api/questions').status_code, 409)
        self.start()
        self.assertEqual(self.client.post('/api/scores').status_code, 409)

    def test_missing_and_invalid_question_files(self):
        self.register()
        os.remove(quiz.QUESTIONS_FILE)
        self.assertEqual(self.client.post('/start').status_code, 503)
        write_text(quiz.QUESTIONS_FILE, "broken JSON")
        self.assertEqual(self.client.post('/start').status_code, 503)

    def test_bad_question_structure(self):
        data = quiz.load_questions()
        first_question = list(data.keys())[0]
        data[first_question]["answers"] = ["not an option"]
        write_text(quiz.QUESTIONS_FILE, json.dumps(data))
        with self.assertRaises(ValueError):
            quiz.load_questions()

    def test_corrupt_scores_are_not_overwritten(self):
        self.finish()
        write_text(quiz.SCORES_FILE, "broken history")
        self.assertEqual(self.client.get('/result').status_code, 503)
        self.assertEqual(read_text(quiz.SCORES_FILE), "broken history")

    def test_save_error_can_be_retried(self):
        self.start()
        for _ in range(4):
            self.answer()
            self.client.post('/next', follow_redirects=True)
        with patch("webapp_quiz.os.replace", side_effect=PermissionError("Cannot save")):
            self.assertEqual(self.answer().status_code, 503)
        self.assertTrue(self.state()["finished"])
        self.assertEqual(self.client.get('/result').status_code, 200)
        self.assertEqual(len(quiz.load_scores()), 1)

    def test_duplicate_choice_does_not_match_two_correct_answers(self):
        self.assertEqual(quiz.calculate_points(["A", "A"], ["A", "B"], 2), 0)
        self.assertEqual(quiz.calculate_points(["A"], ["A", "B"], 2), 0)

    def test_question_file_rejects_repeated_options(self):
        data = quiz.load_questions()
        first_question = list(data.keys())[0]
        item = data[first_question]
        item["options"].append(item["options"][0])
        write_text(quiz.QUESTIONS_FILE, json.dumps(data))
        with self.assertRaises(ValueError):
            quiz.load_questions()

    def test_review_keeps_question_numbers_and_mixed_scores(self):
        self.start()
        for number in range(5):
            if number == 0:
                response = self.answer(self.wrong_answers())
            else:
                response = self.answer()
            if number < 4:
                self.client.post('/next', follow_redirects=True)
        self.assertIn(b"60 / 75", response.data)
        self.assertIn(b"Correct: 4", response.data)
        self.assertIn(b"Incorrect: 1", response.data)
        self.assertIn(b"1. ", response.data)
        self.assertIn(b"5. ", response.data)
        self.assertEqual(quiz.load_scores()[0]["score"], 60)

    def test_stylesheet_and_timer_files_are_available(self):
        # Check the missing-file problem seen while setting up the app.
        for path in ['/static/style.css', '/static/timer.js']:
            response = self.client.get(path)
            try:
                self.assertEqual(response.status_code, 200, path + " was not found")
                self.assertTrue(response.data.strip(), path + " is empty")
                self.assertNotIn("text/html", response.content_type)
            finally:
                response.close()
        response = self.start("challenge")
        self.assertIn(b'/static/style.css', response.data)
        self.assertIn(b'/static/timer.js', response.data)
        self.assertIn(b'id="timer"', response.data)
        self.assertIn(b'id="seconds"', response.data)

    def test_empty_scores_file_shows_a_helpful_error(self):
        self.register()
        write_text(quiz.SCORES_FILE, "")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 503)
        self.assertIn(b'Cannot read or save the quiz data', response.data)
        self.assertEqual(read_text(quiz.SCORES_FILE), "")
        # An empty list is valid JSON and lets the home page load again.
        write_text(quiz.SCORES_FILE, "[]")
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_selection_count_with_real_options(self):
        self.start()
        state = self.state()
        question = state["selected_questions"][0]
        item = quiz.load_questions()[question]
        required = len(item["answers"])
        too_few = item["answers"][:-1]
        too_many = item["options"][:required + 1]
        for answers in [too_few, too_many]:
            response = self.answer(answers)
            self.assertIn(b'Please choose exactly', response.data)
            self.assertEqual(self.state()["question_scores"], {})
            self.assertEqual(self.state()["current_question"], 0)

    def test_start_requires_a_name(self):
        response = self.client.post('/start', data={"mode": "practice"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], '/')
        self.assertNotIn("quiz_id", self.state())


if __name__ == '__main__':
    unittest.main(verbosity=2)
