# Will use English alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Select encode or decode
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# Get text to decode or encode
text = input("Type your message:\n").lower()

# Get shift number
shift = int(input("Type the shift number:\n"))

# Encryption
def encrypt(text, shift):
    """
    Encrypts a given 'text' by replacing all the letters of the text 
    with a letter 'shift' positions up the alphabet. Note that if
    shift = 26, the cipher of any text will be itself.
    
    examples: 
    text = 'abc' shift = 1 --> decoded text = 'bcd',
    text = 'abc' shift = 10 --> decoded text = 'klm',
    text = 'abc' shift = 25 --> decoded text = 'zab',
    text = 'abc' shift = 26 --> decoded text = 'abc', 
    
    :param text: text to decode - string 
    :param shift: cipher amount - int

    """     
  cipher_text = ""
  
  # Replace all the letters by changing the index number to + shift
  # to the right. Note that since there are 26 letters in English we 
  # use modulus operator. 
  for letter in text:
    index = (alphabet.index(letter) + shift) % 26
    cipher_text += alphabet[index]
  print(f"The encoded text is {cipher_text}")

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  print("Not there yet!")
else:
  print("Please type 'encode' or 'decode'")