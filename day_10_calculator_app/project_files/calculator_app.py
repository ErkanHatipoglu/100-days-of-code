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

# get input 1
num1 = int(input("Enter first number: "))

# get operator
operation_symbol = input("Enter operation symbol: ")

# get input 2
num2 = int(input("Enter second number: "))

# define calculation function
calculation_function = operations[operation_symbol]

# make calculation
answer = calculation_function(num1, num2)

# print answer
print(f"{num1} {operation_symbol} {num2} = {answer}")

# get operator
operation_symbol = input("Pick another operation: ")

# get input 3
num3 = int(input("What is the next number?: "))

# define calculation function
calculation_function = operations[operation_symbol]

# make calculation
second_answer = calculation_function(answer, num3)

# print answer
print(f"{answer} {operation_symbol} {num3} = {second_answer}")
