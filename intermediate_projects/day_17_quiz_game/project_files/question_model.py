class Question:
    """
    A class to represent a quiz question.

    Attributes:
        text (str): The text of the quiz question.
        answer (str): The answer to the quiz question (True/False).
    """

    def __init__(self, text, answer):
        """
        The constructor for Question class.

        Parameters:
           text (str): The text of the quiz question.
           answer (str): The answer to the quiz question (True/False).
        """
        self.text = text
        self.answer = answer
