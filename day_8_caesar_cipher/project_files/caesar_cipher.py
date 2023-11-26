# Will use English alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Select encode or decode
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# Get text to decode or encode
text = input("Type your message:\n").lower()

# Get shift number
shift = int(input("Type the shift number:\n"))

# Encryption
def caesar(plain_text, shift_amount, index_direction):

  """
    Encrypts or decrypts a given 'text' by replacing all the letters
    of the text with a letter 'shift' positions up or down the alphabet.
    Note that if shift = 26, the cipher or decryption of any text will
    be itself.

    examples: encode
    text = 'abc' shift = 01 --> decoded text = 'bcd',
    text = 'abc' shift = 10 --> decoded text = 'klm',
    text = 'abc' shift = 25 --> decoded text = 'zab',
    text = 'abc' shift = 26 --> decoded text = 'abc',
    
    examples: decode
    text = 'abc' shift = 01 --> encoded text = 'zab',
    text = 'abc' shift = 10 --> encoded text = 'qrs',
    text = 'abc' shift = 25 --> encoded text = 'bcd',
    text = 'abc' shift = 26 --> encoded text = 'abc', 

    :param plain_text: text to decode or encode - string 
    :param shift_amount: cipher amount - int
    :param index_direction: shift direction - string

  """
  caesar_text = ""
  is_valid_direction = False
  
  # For encoding, the shift will be to the positive direction, 
  # whereas for decoding the shift will be in the negative direction.
  # if the direction is not written properly no calculations will be
  # made! 
  if index_direction == "encode":
    shift_amount = shift
    is_valid_direction = True
  elif index_direction == "decode":
    shift_amount = -shift
    is_valid_direction = True
  else:
    is_valid_direction = False
    print("Please type 'encode' or 'decode'")
 
  # Replace all the letters by changing the index number to + shift
  # to the right or left. Note that since there are 26 letters in
  # English we use the modulus operator. 
  if is_valid_direction:
    for letter in plain_text:
      index = (alphabet.index(letter) + shift_amount) % 26
      caesar_text += alphabet[index]
    print(f"The {index_direction}d text is {caesar_text}")

caesar(plain_text = text, shift_amount = shift, index_direction = direction)