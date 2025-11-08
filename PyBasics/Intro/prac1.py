# CHAPTER 1: EXERCISE 1.8     (SAT/08/11/2025)
print('1.', 'Print a box like the one below.')
print('*' * 19)
print('*' * 19)
print('*' * 19)
print('*' * 19)

print('2.', 'Print a box like the one below.')
print('*' * 19)
print('*', ' '*17, '*', sep='')
print('*', ' '*17, '*', sep='')
print('*' * 19)

print('3.', 'Print a triangle like the one below.')
print('*')
print('*'*2)
print('*'*3)
print('*'*4)

print('4.', 'Write a program that computes and prints the result of ' '512-282/47*48+5')
num1 = eval(input('Enter the first number:'))
num2 = eval(input('Enter the second number:'))
print(num1/num2)


print('5.', 'Print out the square of a number, but use the sep optional argument to print it out in a full sentence that ends in a period.')
num = eval(input('Enter a number: '))
print('Your number squared:', num*num)

print('6.', 'Use the sep optional argument to print out x, 2x, 3x, 4x, and 5x, each separated by three dashes.')
num = eval(input('Enter a number:'))
print(num, 2*num, 3*num, 4*num, 5*num, sep='---',)

print('7.', 'Write a program that asks the user for a weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram.')
kilo = eval(input('Enter a weight in kilogram:'))
pounds_kilo = 11/5*kilo
print('In Pounds, that is', pounds_kilo)

print('8.', 'Write a program that asks the user to enter three numbers')
num1 = eval(input('Enter the first number:'))
num2 = eval(input('Enter the second number:'))
num3 = eval(input('Enter the third number:'))
print('Total =', (num1+num2+num3))
print('Average =', (num1+num2+num3)/2)

print('9.', 'Ask the user for the price of the meal and the percentage tip they want to leave.')
num1 = eval(input('Enter the price:'))
num2 = eval(input('Enter 5 percent tip:'))
print('Total =', (num1*1.05))

num3 = eval(input('Enter the price2:'))
num4 = eval(input('Enter 10 percent tip:'))
print('Total =', (num3*1.1))


# CORRECTION FOR NUMBER 9:
food_price = eval(input('Enter the meal amount:'))
tip = eval(input('Enter the tip you want to leave in percentage:'))
total = food_price + food_price*tip/100

print('The tip was', tip, 'percent and the total bill is', total)

print(f'The tip was {tip}% and the total is N{total}')
