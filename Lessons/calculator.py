# SIMPLE CALCULATOR

# First,show the user the operations the calculator can perform.

'''
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

'''

# Use input() to get the user's choice.

'''
choice = input("Enter choice (1/2/3/4): ")

'''

# Ask the user for the two numbers they want to perform the operation on.

'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

'''

# We use float() so that the user can enter decimal numbers as well.
# Use if-elif statements to perform the operation based on the user's choice.

'''
if choice == '1':
    result = num1 + num2
    print("Result:", result)
elif choice == '2':
    result = num1 - num2
    print("Result:", result)
elif choice == '3':
    result = num1 * num2
    print("Result:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input")

'''

##############################################################
# Better way to do this is to use a function for each operation,
# and then call the function based on the user's choice, for example:

'''
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("1:Add 2:Subtract 3:Multiply 4:Divide")

choice = input("Enter choice: ")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(subtract(num1, num2))
elif choice == '3':
    print(multiply(num1, num2))
elif choice == '4':
    print(divide(num1, num2))

'''

# Loop Calculator in Python:
# A loop calculator is a calculator that allows the user to perform multiple calculations without having to restart the program, for example:

# Start with a loop:
# We use a while loop to keep the calculator running until the user decides to exit, for example:

'''
while True:

# Show the calculator menu:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
# Ask the user for their choice:
    choice = input("Enter choice (1-5): ")
    
# Add an option to exit the calculator:
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
        
# Get the numbers from the user:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
# Perform the calculation based on the user's choice:
    if choice == '1':
        result = num1 + num2
        print("Result:", result)
        
    elif choice == '2':
        result = num1 - num2
        print("Result:", result)
        
    elif choice == '3':
        result = num1 * num2
        print("Result:", result)
        
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please enter a number between 1 and 5.")

'''
