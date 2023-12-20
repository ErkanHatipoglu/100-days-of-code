"""
This module serves as the main entry point for the quiz application. It utilizes the
Question model from 'question_model.py', question data from 'data.py', and the QuizBrain
class from 'quiz_brain.py' to create a quiz game. It sets up the question bank and controls
the quiz flow.
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
