import pandas as pd

student_dict = {
    "student":["Angela", "James", "Lily"], "score":[56, 76, 98] }

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    print(f"key: {key}, value: {value}")

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score

    print(f"Index: {index}; Student: {row.student}; Score: {row.score}")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:

# Read the csv file
nato_phonetic_df = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the DataFrame
letter_to_phonetic_dict = { row.letter:row.code for (index, row) in nato_phonetic_df.iterrows() }

# Test
print(letter_to_phonetic_dict)

{ "A":"Alfa", "B":"Bravo" }

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()
letter_to_phonetic_list = [letter_to_phonetic_dict[letter] for letter in user_input]
print(letter_to_phonetic_list)
