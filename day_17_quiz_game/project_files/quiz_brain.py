class QuizBrain:
    """
    A class to manage the quiz game logic.

    Attributes:
        question_number (int): Tracks the current question number in the quiz.
        question_list (list): A list of Question objects to be used in the quiz.
    """

    def __init__(self, question_list):
        """
        The constructor for the QuizBrain class.

        Parameters:
            question_list (list): A list of Question objects for the quiz.
        """
        self.question_number = 0  # Initialize the question number to zero
        self.question_list = question_list  # Store the provided list of questions

    def next_question(self):
        """
        Presents the next question to the user and increments the question number.
        """
        # Retrieve the next question from the list
        new_question = self.question_list[self.question_number]
        question_text = new_question.text
        self.question_number += 1  # Increment the question number

        # Display the question and prompt for user's answer
        input(f"Q.{self.question_number}: {question_text} (True/False):")

    def still_has_questions(self):
        """
        Determines if there are more questions remaining in the quiz.

        Returns:
            bool: True if more questions are remaining, False otherwise.
        """
        # Check if there are more questions in the list
        return self.question_number < len(self.question_list)
