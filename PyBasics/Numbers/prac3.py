# CHAPTER 3: NUMBERS IN PYTHON
# EXERCISE 3.8
# print('1.','Write a program that generates and prints 50 random integers, each between 3 and 6.')
# from random import randint
# x = randint(3,6)
# print('A random number between 3 and 6: ', x)


# print('2.','Write a program that generates a random number, x between 1 and 50, a random number y between 2 and 5, and computes x^y.')
# from random import randint
# x = randint(1,50)
# print('A random number between 1 and 50: ', x)

# y = randint(2, 5)
# print('A random number between 2 and 5: ', y)

# import math
# print('Therefore x to the power of y equals: ', math.pow(x,y))


# print('3.','Write a program that generates a random number between 1 and 10 and prints your name that many times')
# import random
# x = random.randint(1,10)
# print('A random number between 1 and 10: ', x)
# for i in range(x):
#     print('Henry')


# print('4.', 'Write a program that generates a random decimal number between 1 and 10 with two decimal places of accuracy.
# Examples are 1.23, 3.45, 9.80, and 5.00.')
# import random
# x = round(random.uniform(1, 10), 2)
# print(f"Random Decimal Number: {x}")


# revisit
# print('5.', 'Write a program that generates 50 random numbers such that the first number is between 1 and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between 1 and 51.')
# import random
# x = randint(1,2)
# print('A random number between 1 and 2: ', x)
# x = randint(1,3)
# print('A random number between 1 and 3: ', x)
# x = randint(1,4)
# print('A random number between 1 and 4: ', x)
# x = randint(1,51)
# print('A random number between 1 and 51: ', x)


# print('6.' 'Write a program that asks the user to enter two numbers, x and y, and computes |x−y|/x+y.')
# x = float(input('Type the value of x: '))
# y = float(input('Type the value of y: '))
# z = abs(x - y)/(x + y)
# print(f"The result is: {z:.2f}")


# print('7.' 'Write a program that asks the user to enter an angle between −180◦ and 180◦.
# Using an expression with the modulo operator, convert the angle to its equivalent between 0◦ and 360◦')

# Get the user to input the value for the angle
# angle = float(input('Type an angle between -180 and 180 degrees: '))
# Use the modulo operator to convert the angle to its equivalent btw 0 and 360 degrees
# x = angle % 360
# print(f'The equivalent angle is: {x:.2f} degrees')


# print('8.' 'Write a program that asks the user for a number of seconds and prints out how many minutes
# and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the // operator
# to get minutes and the % operator to get seconds.]')

# Get user input for the number of seconds
# a = number_of_seconds
# b = remaining_seconds

# a = int(input("Enter the number of seconds: "))

# # Calculate minutes and remaining seconds
# minutes = a // 60
# b = a % 60

# print(f"{a} seconds is {minutes} minutes and {b} seconds.")


# print('9.' 'Write a program that asks the user for an hour between 1 and 12 and for how many hours in
# the future they want to go. Print out what the hour will be that many hours into the future.
# An example is shown below.
# Enter hour: 8
# How many hours ahead? 5
# New hour: 1 o'clock')

'''
#Get user to enter an hour btw 1 and 12
x = int(input('Enter hour (btw 1 and 12): ')) # x = current_hour
y = int(input('How many hours ahead?: '))     # y = hours_ahead
z = (x + y) % 12                              # z = new_hour
if z == 0:
   z = 12
print(f"New hour: {z} o'clock")

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
