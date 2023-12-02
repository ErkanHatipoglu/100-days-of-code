from art import logo
# Summation

def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

# Define operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
  #dislay logo
  print(logo)
  
  # finish calculation
  is_finished = False

  # get the first input
  num1 = int(input("What is first number?: "))

  # Display operations
  for key in operations:
    print(key)

  # get the operation
  operation_symbol = input("Enter operation symbol: ")

  while not is_finished:
    # get the next input
    num = int(input("What is the next number?: "))

    # define calculation function
    calculation_function = operations[operation_symbol]

    # make calculation
    answer = calculation_function(num1, num)

    # print answer
    print(f"{num1} {operation_symbol} {num} = {answer}")

    # Ask for continue
    user_response = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation.: ")

    if user_response == "y":

      # get the operation
      operation_symbol = input("Pick another operation: ")

      # store previous answer
      num1 = answer

    elif user_response == "n":
      is_finished = True
      calculator()
calculator()
print("Bye")
