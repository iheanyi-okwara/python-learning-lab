# THE IF STATEMENT
'''
##########################################
if grade > 100: # False of True
    print('Yes')
else:
    print('No')

##########################################

'''
'''
score = eval(input('Enter your score: '))

if score >= 80:
    print('Your grade is A')

if score >= 60 and score < 80:
    print('Your grade is B')

if score >= 50 and score < 60:
    print('Your grade is C')

if score >= 40 and score < 50:
    print('Your grade is D')

if score >= 30 and score < 40:
    print('Your grade is E')

if score < 30:
    print('Your grade is F')

'''

# OR
# This is a better way of handling if statements
# when they are connected

'''
score = eval(input('Enter your score: '))
if score >= 80:
    print('Your grade is A')

elif score >= 60 and score < 80:
    print('Your grade is B')

elif score >= 50 and score < 60:
    print('Your grade is C')

elif score >= 40 and score < 50:
    print('Your grade is D')

elif score >= 30 and score < 40:
    print('Your grade is E')

else:
    print('Your grade is F')

'''

# APPROACH TO EX4.5 1
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

'''
# def centimeters_to_inches(length_in_cm):
#     inches = length_in_cm / 2.54
#     return inches

# def main():
#     try:
#         # Get user input for length in centimeters
#         length_in_cm = float(input("Enter length in centimeters: "))

#         # Check if the length is negative
#         if length_in_cm < 0:
#             print("Invalid entry. Length cannot be negative.")
#         else:
#             # Convert length to inches and print the result
#             inches = centimeters_to_inches(length_in_cm)
#             print(f"{length_in_cm} centimeters is equal to {inches:.2f} inches.")
#     except ValueError:
#         # Handle non-numeric input
#         print("Invalid input. Please enter a numeric value.")

# if __name__ == "__main__":
#     main()

'''

'''
# Get temperature input from the user
temperature_celsius = float(input("Enter the temperature in Celsius: "))

# Check if the temperature is below absolute zero
if temperature_celsius < -273.15:
    print("Invalid temperature! It is below absolute zero.")
else:
    # Print a message based on the temperature
    if temperature_celsius < 0:
        print("It's a cold day!")
    elif temperature_celsius >= 0 and temperature_celsius <= 30:
        print("It's a normal day.")
    else:
        print("It's a hot day!")
    
'''
# 2
'''

def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

# Get temperature from user
temperature = float(input("Enter the temperature: "))

# Get unit from user
unit = input("Enter the unit (Celsius or Fahrenheit): ").lower()

# Perform conversion based on the user's input
if unit == 'celsius':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature} Celsius is equal to {converted_temperature} Fahrenheit.")
elif unit == 'fahrenheit':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature} Fahrenheit is equal to {converted_temperature} Celsius.")
else:
    print("Invalid unit. Please enter either Celsius or Fahrenheit.")
'''

'''
# Get temperature input from the user
temperature_celsius = float(input("Enter the temperature in Celsius: "))

# Check and print messages based on the temperature
if temperature_celsius < -273.15:
    print("Invalid temperature! It is below absolute zero.")
elif temperature_celsius == -273.15:
    print("The temperature is absolute 0.")
elif -273.15 < temperature_celsius < 0:
    print("The temperature is below freezing.")
elif temperature_celsius == 0:
    print("The temperature is at the freezing point.")
elif 0 < temperature_celsius < 100:
    print("The temperature is in the normal range.")
elif temperature_celsius == 100:
    print("The temperature is at the boiling point.")
else:
    print("The temperature is above the boiling point.")

'''

# 4.
'''
Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over

'''
'''
# Get credit input from user
credits = float(input('Enter how many credits you have taken: '))

#Check if range is between 54 and 83
if credits > 0 and credits <= 23:
    print('The student is a freshman.')
elif credits >= 24 and credits < 53:
    print('You are a sophomore.')
elif credits >= 54 and credits <= 83:
    print('You are a junior')
else:
    print('You are a senior') 


'''

# 5.
'''
Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.



from random import randint
x = randint(1,10)

# Get a user to guess a number
x2 = float(input('Enter a random number: '))
if x2 == x:
    print('You are correct')
else:
    print('You are wrong. Guess another number')

'''
