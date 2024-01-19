class Question:
    """Called every time you create a new object from this class"""
    def __init__(self, q_text, q_answer):
        """Self is to get hold of the object, then get access to its attributes"""
        self.text = q_text
        self.answer = q_answer
