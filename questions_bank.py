from question_model import Question
from data import question_data


class QuestionsBank:
    def __init__(self):
        self.question_bank = [Question(q_text=q["text"], q_answer=q["answer"]) for q in question_data]

    def get_question_bank(self):
        return self.question_bank
