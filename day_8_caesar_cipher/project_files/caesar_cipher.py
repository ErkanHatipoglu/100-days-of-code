alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Select encode or decode
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# Get text to decode or encode
text = input("Type your message:\n").lower()

# Get shift number
shift = int(input("Type the shift number:\n"))