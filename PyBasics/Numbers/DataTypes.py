# CHAPTER 3: NUMBERS IN PYTHON    (SUN/17/12/2023)
# Data types
'''
Integers - int
floats - float

modulo operator %

5%2=1
i%7=0
4%2=0

integer division
5//2 = 2

math.ceil
2.1=3
math.floor
round

one crate contains 24: 55

2 = 48

3 = 72

2.29 = 3

Namespaces
-builtin namespaces
-global namespace
-enclosed namespace
-local namespace

LEGB

'''

# How to import in python
'''
The core part of the Python language consists of things like for loops, if statements, math operators, and some
functions, like print and input. Everything else is contained in modules, and if we want to use
something from a module we have to first import it—that is, tell Python that we want to use it.

'''
# import math library
# import math
# print(math.sqrt(4))

# #OR
# from math import sqrt
# print(sqrt(4))

# from random import randint
# x = randint(1,10)
# print('A random number between 1 and 10: ', x)


# EXERCISES

# Solution to Exercise 3.8, number 3:
# import random

# def print_name_multiple_times():
#     # Generate a random number between 1 and 10
#     random_number = random.randint(1, 10)

#     # Print your name that many times
#     for _ in range(random_number):
#         print("Your Name")

# if __name__ == "__main__":
#     print_name_multiple_times()


# correction to Exercise 3.8 number 4:
# import random

# def generate_random_decimal():
#     # Generate a random decimal number between 1 and 10 with two decimal places
#     random_decimal = round(random.uniform(1, 10), 2)
#     return random_decimal

# def main():
#     random_decimal = generate_random_decimal()
#     print(f"Random Decimal Number: {random_decimal}")

# if __name__ == "__main__":
#     main()


# solution to number 5:
'''
import random

def generate_random_numbers():
    random_numbers = []

    for i in range(1, 51):
        # Generate a random number between 1 and (i + 1)
        random_number = random.uniform(1, i + 1)
        random_numbers.append(random_number)

    return random_numbers

def main():
    # Generate 50 random numbers according to the specified pattern
    numbers = generate_random_numbers()

    # Print the generated numbers
    for i, number in enumerate(numbers, start=1):
        print(f"Number {i}: {number:.2f}")

if __name__ == "__main__":
    main()

'''


# solution to number 6:
'''
def calculate_expression():
    try:
        # Get user input for two numbers, x and y
        x = float(input("Enter the value for x: "))
        y = float(input("Enter the value for y: "))

        # Compute the expression |x - y| / (x + y)
        result = abs(x - y) / (x + y)

        print(f"The result of |x - y| / (x + y) is: {result:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculate_expression()

'''

# SOLUTION TO QUESTION 7:
# print('7.' 'Write a program that asks the user to enter an angle between −180◦ and 180◦.
# Using an expression with the modulo operator, convert the angle to its equivalent between 0◦ and 360◦')

'''
#correction
def convert_angle():
    try:
        # Get user input for the angle
        angle = float(input("Enter an angle between -180 and 180 degrees: "))

        # Use the modulo operator to convert the angle to its equivalent between 0 and 360 degrees
        converted_angle = angle % 360

        print(f"The equivalent angle between 0 and 360 degrees is: {converted_angle:.2f} degrees")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    convert_angle()

'''

# print('8.' 'Write a program that asks the user for a number of seconds and prints out how many minutes
# and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the // operator
# to get minutes and the % operator to get seconds.]')

'''
def convert_seconds_to_minutes_and_seconds():
    try:
        # Get user input for the number of seconds
        total_seconds = int(input("Enter the number of seconds: "))

        # Calculate minutes and remaining seconds
        minutes = total_seconds // 60
        remaining_seconds = total_seconds % 60

        print(f"{total_seconds} seconds is {minutes} minutes and {remaining_seconds} seconds.")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of seconds.")

if __name__ == "__main__":
    convert_seconds_to_minutes_and_seconds()

'''

# solution to question 9:

'''
def calculate_future_hour():
    try:
        # Get user input for the current hour
        current_hour = int(input("Enter the current hour (between 1 and 12): "))

        # Validate input for the current hour
        if current_hour < 1 or current_hour > 12:
            print("Invalid input. Please enter an hour between 1 and 12.")
            return

        # Get user input for the number of hours into the future
        hours_ahead = int(input("How many hours ahead? "))

        # Calculate the new hour
        new_hour = (current_hour + hours_ahead) % 12

        # Adjust for midnight (new_hour should be 12 instead of 0)
        if new_hour == 0:
            new_hour = 12

        print(f"New hour: {new_hour} o'clock")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    calculate_future_hour()

'''


# 10
# (a) One way to find out the last digit of a number is to mod the number by 10. Write a
# program that asks the user to enter a power. Then find the last digit of 2 raised to that
# power.

'''
def last_digit_of_power():
    try:
        # Get user input for the power
        power = int(input("Enter a power: "))

        # Calculate and print the last digit of 2 raised to the power
        last_digit = 2 ** power % 10
        print(f"The last digit of 2^{power} is: {last_digit}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

if __name__ == "__main__":
    # Part (a)
    last_digit_of_power()

# (b) One way to find out the last two digits of a number is to mod the number by 100. Write
# a program that asks the user to enter a power. Then find the last two digits of 2 raised to
# that power.
        
def last_two_digits_of_power():
    try:
        # Get user input for the power
        power = int(input("Enter a power: "))

        # Calculate and print the last two digits of 2 raised to the power
        last_two_digits = 2 ** power % 100
        print(f"The last two digits of 2^{power} are: {last_two_digits:02d}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

if __name__ == "__main__":
    # Part (b)
    last_two_digits_of_power()


# (c) Write a program that asks the user to enter a power and how many digits they want.
# Find the last that many digits of 2 raised to the power the user entered.

def last_n_digits_of_power():
    try:
        # Get user input for the power and number of digits
        power = int(input("Enter a power: "))
        num_digits = int(input("Enter the number of digits you want: "))

        # Calculate and print the last n digits of 2 raised to the power
        last_digits = 2 ** power % 10 ** num_digits
        print(f"The last {num_digits} digits of 2^{power} are: {last_digits:0{num_digits}d}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    # Part (c)
    last_n_digits_of_power()
'''

# 11
# print('11.' 'Write a program that asks the user to enter a weight in kilograms. The program should
# convert it to pounds, printing the answer rounded to the nearest tenth of a pound.')

'''
def kg_to_pounds(kilograms):
    pounds = kilograms * 2.20462  # 1 kilogram is approximately 2.20462 pounds
    return pounds

def main():
    try:
        # Get user input for weight in kilograms
        weight_kg = float(input("Enter weight in kilograms: "))

        # Convert kilograms to pounds and round to the nearest tenth
        weight_pounds = round(kg_to_pounds(weight_kg), 1)

        # Print the result
        print(f"{weight_kg} kilograms is approximately {weight_pounds} pounds.")
    
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for weight.")

if __name__ == "__main__":
    main()

'''

# Question 12
# Write a program that asks the user for a number and prints out the factorial of that number

'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        # Get user input for a number
        user_number = int(input("Enter a number: "))

        # Check if the number is non-negative
        if user_number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            # Calculate factorial and print the result
            result = factorial(user_number)
            print(f"The factorial of {user_number} is: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

'''

# 13
# Write a program that asks the user for a number and then prints out the sine, cosine, and
# tangent of that number.

'''
import math

def trig_functions(number):
    # Convert degrees to radians since trigonometric functions in Python use radians
    radians = math.radians(number)

    # Calculate sine, cosine, and tangent
    sine_value = math.sin(radians)
    cosine_value = math.cos(radians)
    
    # Check if tangent is undefined for certain angles (e.g., 90 degrees)
    if abs(math.cos(radians)) < 1e-10:
        tangent_value = "Undefined"
    else:
        tangent_value = math.tan(radians)

    return sine_value, cosine_value, tangent_value

def main():
    try:
        # Get user input for a number
        user_number = float(input("Enter a number in degrees: "))

        # Calculate trigonometric values
        sine, cosine, tangent = trig_functions(user_number)

        # Print the results
        print(f"Sine({user_number} degrees): {sine}")
        print(f"Cosine({user_number} degrees): {cosine}")
        print(f"Tangent({user_number} degrees): {tangent}")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

if __name__ == "__main__":
    main()

'''

# 14
# Write a program that asks the user to enter an angle in degrees and prints out the sine of that angle.


def calculate_sine(angle_degrees):
    # Convert degrees to radians since the math.sin function in Python uses radians
    radians = math.radians(angle_degrees)

    # Calculate sine
    sine_value = math.sin(radians)

    return sine_value


def main():
    try:
        # Get user input for an angle in degrees
        user_angle = float(input("Enter an angle in degrees: "))

        # Calculate sine and print the result
        sine_result = calculate_sine(user_angle)
        print(f"The sine of {user_angle} degrees is: {sine_result}")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")


if __name__ == "__main__":
    main()
