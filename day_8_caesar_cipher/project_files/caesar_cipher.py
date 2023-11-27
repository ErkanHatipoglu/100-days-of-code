from art import logo

# print logo
print(logo)

# Will use English alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

quit_cipher = False
is_valid_decision = True

# Ciphering
def caesar(start_text, shift_amount, cipher_direction):
    """
    Encrypts or decrypts a given 'start_text' by replacing all the letters of the text 
    with a letter 'shift_amount' positions up or down the alphabet. Note that if
    shift_amount = 26, the end_text of any 'start_text' will be itself.

    examples: encode
    text = 'abc' shift_amount = 01 --> decoded text = 'bcd',
    text = 'abc' shift_amount = 10 --> decoded text = 'klm',
    text = 'abc' shift_amount = 25 --> decoded text = 'zab',
    text = 'abc' shift_amount = 26 --> decoded text = 'abc',

    examples: decode
    text = 'abc' shift_amount = 01 --> encoded text = 'zab',
    text = 'abc' shift_amount = 10 --> encoded text = 'qrs',
    text = 'abc' shift_amount = 25 --> encoded text = 'bcd',
    text = 'abc' shift_amount = 26 --> encoded text = 'abc', 

    :param start_text: text to decode or encode - string 
    :param shift_amount: cipher amount - int
    :param cipher_direction: shift direction - string

  """
    end_text = ""
    is_valid_direction = False

    # For encoding, the shift will be to the positive direction,
    # whereas for decoding the shift will be in the negative direction.
    if cipher_direction == "encode":
        shift_amount = shift
        is_valid_direction = True
    elif cipher_direction == "decode":
        shift_amount = -shift
        is_valid_direction = True
    else:
        is_valid_direction = False
        print("Please type 'encode' or 'decode'")

    # Replace all the letters by changing the index number to + shift
    # to the right or left. Note that since there are 26 letters in English
    # we use the modulus operator.
    if is_valid_direction:
        for letter in start_text:
            if letter in alphabet:
                index = (alphabet.index(letter) + shift_amount) % 26
                end_text += alphabet[index]
            else:
                end_text += letter
        print(f"The {cipher_direction}d text is {end_text}")

while not quit_cipher:
    # Select encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # Get text to decode or encode
    text = input("Type your message:\n").lower()

    # Get shift number
    shift = int(input("Type the shift number:\n"))

    # Call caesar function
    if is_valid_decision:
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask user if they want to quit or continue
    decision = input(
        "Type 'yes' if you want to continue ciphering. Type 'no' to quit.\n"
    ).lower()

    # Quit or continue ciphering
    if decision == "yes":
        quit_cipher = False
        is_valid_decision = True
    elif decision == "no":
        quit_cipher = True
        is_valid_decision = True
        print("Thanks for using the Caesar Cipher!")
    else:
        print("Please type 'yes' or 'no'.")
        quit_cipher = False
        is_valid_decision = False