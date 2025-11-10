# 1

# Write a program that asks the user to enter a length in centimeters. If the user enters a negative
# length, the program should tell the user that the entry is invalid. Otherwise, the program
# should convert the length to inches and print out the result. There are 2.54 centimeters in an
# inch
'''
length = eval(input('Enter length in cm: '))
if length < 0:
    print('You entered an invalid number')
else:
    inch = length/2.54
    print('{}cm is equal to {} inches' .format(length, inch))
'''

# 2.
'''
def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32
def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

# Get temperature input from user
temp = eval(input('Enter a temperature: '))

#Get unit from user
unit = input('Enter what unit, Celsius or Fahrenheit: ').lower()
if unit == 'celsius':
    New_temp = celsius_to_fahrenheit(temp)
    print(f"{temp} degree Celsius is equal to {New_temp} Fahrenheit")
elif unit == 'fahrenheit':
    New_temp = fahrenheit_to_celsius(temp)
    print(f"{temp} Fahrenheit is equal to {New_temp} Celsius")
else:
    print('Invalid unit. Please enter either celsius or fahrenheit.')

'''

# 3.
'''
temp = eval(input('Enter temperature in Celsius: '))
if temp < -273.15:
    print('The temperature is invalid number because it is below absolute zero.')
elif temp == -273.15:
    print("The temperature is absolute 0.")
elif -273.15 < temp < 0:
    print("Temperature is below freezing.")
elif temp == 0:
    print('Temperature is at the freezing point.')
elif 0 < temp < 100:
    print('The temperature is normal.')
elif temp == 100:
    print('The temperature is at the boiling point.')
else:
    print('The temperature is above the boiling point.')
'''

# 4
# Write a program that asks the user how many credits they have taken. If they have taken 23
# or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.

# Get credit input from user
from random import randint
credits = float(input('Enter how many credits you have taken: '))

# Check if range is between 54 and 83
if credits > 0 and credits <= 23:
    print('The student is a freshman.')
elif credits >= 24 and credits < 53:
    print('You are a sophomore.')
elif credits >= 54 and credits <= 83:
    print('You are a junior')
else:
    print('You are a senior')


# 5.
'''
Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.
'''

x = randint(1, 10)

# Get a user to guess a number
x2 = float(input('Enter a random number: '))
if x2 == x:
    print('You are correct')
else:
    print('You are wrong. Guess another number')
