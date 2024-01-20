import unittest
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from questions_bank import QuestionsBank

NR_QUESTIONS_EXPECTED = len(QuestionsBank().get_question_bank())
SCORE_EXPECTED = 0
QUESTION_NR_EXPECTED = 0


class TestQuizBrain(unittest.TestCase):
    def setUp(self):
        question_bank = QuestionsBank().get_question_bank()
        self.quiz = QuizBrain(question_bank)

    def test_initialization(self):
        self.assertEqual(self.quiz.question_number, QUESTION_NR_EXPECTED)
        self.assertEqual(self.quiz.score, SCORE_EXPECTED)
        self.assertEqual(len(self.quiz.questions_list), NR_QUESTIONS_EXPECTED)

    def test_still_has_question(self):
        self.assertTrue(self.quiz.still_has_question())
        # Assuming the quiz has been set up with 12 questions, let's answer all of them
        for _ in range(NR_QUESTIONS_EXPECTED):
            self.quiz.next_question()
        self.assertFalse(self.quiz.still_has_question())  # After answering all questions, there should be none left

    def test_check_answer_correct(self):
        # Assuming the correct answer is "True" for the first question
        self.quiz.check_answer("True", "True")
        self.assertEqual(self.quiz.score, 1)

    def test_check_answer_incorrect(self):
        # Assuming the correct answer is "True" for the first question
        self.quiz.check_answer("False", "True")
        self.assertEqual(self.quiz.score, 0)

    def test_check_answer_empty_quiz(self):
        # Create an empty quiz
        empty_quiz = QuizBrain([])

        # Attempt to check an answer in an empty quiz
        empty_quiz.check_answer("True", "True")

        # Ensure that the score remains 0 in an empty quiz
        self.assertEqual(empty_quiz.score, 0)
