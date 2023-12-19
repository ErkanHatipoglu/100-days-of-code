"""
This module serves as the main entry point for the quiz application. It utilizes the
Question model from 'question_model.py' and question data from 'data.py' to create
a list of question objects and display them for testing purposes.
"""

from question_model import Question  # Importing the Question class to create question objects
from data import question_data  # Importing quiz data to populate the questions

# Initialize an empty list to store question objects
question_bank = []
for dict in question_data:
    # Creating a Question object from each dictionary in question_data
    my_question = Question(dict["text"], dict["answer"])
    question_bank.append(my_question)

# Testing block to display each question and its corresponding answer
num = 1
for q in question_bank:
    print(f"Question-{num}: {q.text} ")
    print(f"Answer-{num}: {q.answer} ")
    print()
    num += 1