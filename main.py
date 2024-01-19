from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = [Question(q_text=q["text"], q_answer=q["answer"]) for q in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/12")