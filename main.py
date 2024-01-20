from quiz_brain import QuizBrain
from questions_bank import QuestionsBank
question_bank = QuestionsBank().get_question_bank()

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/12")