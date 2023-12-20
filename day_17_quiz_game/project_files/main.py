"""
This module serves as the main entry point for the quiz application. It utilizes the
Question model from 'question_model.py', question data from 'data.py', and the QuizBrain
class from 'quiz_brain.py' to create a quiz game. It sets up the question bank, controls
the quiz flow, and displays the final score.
"""

from question_model import Question  # Importing the Question class to create question objects
from data import question_data  # Importing quiz data to populate the questions
from quiz_brain import QuizBrain  # Importing the QuizBrain class to manage quiz logic

# Initialize an empty list to store question objects
question_bank = []
for dict in question_data:
    # Creating a Question object from each dictionary in question_data
    new_question = Question(dict["text"], dict["answer"])
    question_bank.append(new_question)

# Initialize the QuizBrain object with the question bank
quiz_brain = QuizBrain(question_bank)

# Loop through all questions in the quiz
while quiz_brain.still_has_questions():
    quiz_brain.next_question()  # Present each question to the user

# Display the user's final score after completing the quiz
print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{len(question_bank)}")