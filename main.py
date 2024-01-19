# class User:
#     """Called every time you create a new object from this class"""
#     def __init__(self, name, id):
#         """Self is to get hold of the object, then get access to its attributes"""
#         print("New user being created...")
#         self.name = name
#         self.id = id
#         print("New user created successfully")
#
# user1 = User("Rawad", 200)
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)
print(question_bank)
quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/12")