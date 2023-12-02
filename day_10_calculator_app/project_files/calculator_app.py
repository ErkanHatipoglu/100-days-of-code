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

# finish calculation
is_finished = False

# get the first input
num1 = int(input("What is first number?: "))

# get the operation
operation_symbol = input("Enter operation symbol: ")

# get the second input
num2 = int(input("What is the next number?: "))

# define calculation function
calculation_function = operations[operation_symbol]

# make calculation
answer = calculation_function(num1, num2)

# print answer
print(f"{num1} {operation_symbol} {num2} = {answer}")

while not is_finished:
  # Ask for continue
  user_response = input("Type 'y' to continue calculating with {second_answer}, or 'n' to exit.: ")
  
  if user_response == "y":

    # store previous answer
    prev_answer = answer
    
    # get the operation
    operation_symbol = input("Pick another operation!!!!: ")
    
    # get the input 
    num = int(input("What is the next number?: "))
    
    # define calculation function
    calculation_function = operations[operation_symbol]

    # make calculation
    answer = calculation_function(prev_answer, num)

    # print answer
    print(f"{prev_answer} {operation_symbol} {num} = {answer}")
  
  elif user_response == "n":
    is_finished = True

print("Bye")