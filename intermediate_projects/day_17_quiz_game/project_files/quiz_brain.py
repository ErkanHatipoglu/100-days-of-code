class QuizBrain:
    """
    A class to manage the quiz game logic.

    Attributes:
        question_number (int): Tracks the current question number in the quiz.
        question_list (list): A list of Question objects to be used in the quiz.
        score (int): Tracks the user's score based on correct answers.
    """

    def __init__(self, question_list):
        """
        The constructor for the QuizBrain class.

        Parameters:
            question_list (list): A list of Question objects for the quiz.
        """
        self.question_number = 0  # Initialize the question number to zero
        self.question_list = question_list  # Store the provided list of questions
        self.score = 0  # Initialize the user score to zero

    def next_question(self):
        """
        Presents the next question to the user, prompts for an answer, and checks it.
        """
        # Retrieve the next question from the list
        new_question = self.question_list[self.question_number]
        question_text = new_question.text
        question_answer = new_question.answer
        self.question_number += 1  # Increment the question number

        # Display the question and prompt for user's answer
        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False):")
        self.check_answer(user_answer, question_answer)

    def still_has_questions(self):
        """
        Determines if there are more questions remaining in the quiz.

        Returns:
            bool: True if more questions are remaining, False otherwise.
        """
        # Check if there are more questions in the list
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks the user's answer against the correct answer and updates the score.

        Parameters:
            user_answer (str): The answer given by the user.
            correct_answer (str): The correct answer for the question.
        """
        # Compare user's answer with the correct answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")

        # Display the correct answer and the user's current score
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print()
