# CHAPTER 5: MISCELLANEOUS TOPICS
# 1 counting
# 2 summing
# 3 swapping
# 4 flag variables
# 5 max and min
# 6 simple debugging


# 1: COUNTING
'''
count = 0
for i in range(1, 1001):
    if i%7 == 0:
        count = count + 1
        #count += 1 |This expression is the same as above|
    print(count)
'''

'''
count = count -1 
#count -= 1  |This expression is the same as above|

1,2,3,4,5
s = 0
for loop
    s = 0 + 1
    s = 1 + 2 =3
    s = 3 + 3 = 6
    s = 6 + 4 = 10
    s = 10 + 5 = 15
'''

# Practice:
'''
Example 1: This program gets 10 numbers from the user and counts how many of those numbers
are greater than 10.

count = 0
for i in range(10):
    num = eval(input('Enter a number: '))
    if num>10:
        count=count+1
print('There are', count, 'numbers greater than 10.')
'''


# Practice2
'''
Example 2 This modification of the previous example counts how many of the numbers the user
enters are greater than 10 and also how many are equal to 0. To count two things we use two count
variables.

count1 = 0
count2 = 0
for i in range(10):
    num = eval(input('Enter a number: '))
    if num>10:
        count1=count1+1
    if num==0:
        count2=count2+1
print('There are', count1, 'numbers greater than 10.')
print('There are', count2, 'zeroes.')
'''

# Practice3
'''
Example 3 Next we have a slightly trickier example. This program counts how many of the
squares from 1**2 to 100**2 end in a 4

count = 0
for i in range(1,101):
    if (i**2)%10==4:
        count = count + 1
print(count)
'''

# 2: SUMMING
# Practice4
'''
Example 1 This program will add up the numbers from 1 to 100. The way this works is that each
time we encounter a new number, we add it to our running total, s

s = 0
for i in range(1,101):
    s = s + i
print('The sum is', s)
'''

# Practice5
'''
Example 2 This program that will ask the user for 10 numbers and then computes their average.

s = 0
for i in range(10):
    num = eval(input('Enter a number: '))
    s = s + num
print('The average is', s/10)
'''


# Practice6
'''
sum_odd = 0
for i in range(1, 101):
    if i%2 != 0:
        sum_odd = sum_odd + i
print('The sum is', sum_odd)
'''

'''
1/1 + 1/2 + 1/3 + 1/4 + 1/5
n = 5
sum_num = 0
for i in range(1, n+1):
    sum_sum = sum_num + 1/i
print(sum_sum)
'''


# 3: SWAPPING
# |To achieve swapping, you have to introduce a temporary holding variable 'temp'|
x = 3
y = 7

temp = x  # temp = 3
x = y     # x = 7
x = temp  # y = 3

x, y = y, x  # |This synthax also works for swapping in python|


# FLAG VARIABLES
'''
flag = False

for i in range(10):
    if i%7 == 0:
        flag = True

if flag == True: #To simplify this you could write
    pass         # if flag:
else:            #     pass
    pass         # else:
                 #     pass
'''


# A flag variable can be used to let one part of your program know when something happens in
# another part of the program. Here is an example that determines if a number is prime.

'''
num = eval(input('Enter number: '))
flag = 0
for i in range(2, num):
    if num%i==0:
        flag = 1

if flag == 1:
    print('Not prime')
else:
    print('Prime')
'''


# MAX AND MIN
'''
[1,2,7,0,49,56,3,4]
max = eval(input('Enter number: ')) # make the first input to be the max
for j in range(4):
    num = eval(input('Enter number: '))
    if num > max:
        max = num
print(f'The maximum number is {max}')
'''


# comment

'''
What makes a code good?
1. Readable
2. Scaleable

'''

# simple debugging
'''
Here are two simple techniques for figuring out why a program is not working:
    1. Use the Python shell.
    2. Add print statements to your program.
    3. An empty input statement, like below, can be used to pause your program at a specific point:
    input()

flag = 0
num = eval(input('Enter number: '))
for i in range(2,num):
    if num%i==0:
        flag = 1
    print(i, flag)
'''

# 1
'''
1. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
1

count = 0
for i in range(1, 101):
    if (i**2)% 10==1:
        count=count+1
print(count)
'''


'''
from random import randint
count = 0
for i in range(10000):
    num = randint(1, 100)
    if num%12==0:
        count=count+1
print('Number of multiples of 12:', count)
'''

'''
CHAPTER 5
EXERCISE 5.9
4. Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000


sum_odd = 0
sum_even = 0
for i in range(1,2001):
    if i%2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i

ans = sum_odd - sum_even

print(ans)
'''

# OR
'''
sum_all = 0
for i in range(1,2001):
    if i%2 == 0:
        sum_all -= i
    else:
        sum_all += i

print(sum_all)
'''


# 14
'''
from random import shuffle, choice

ch = ['g1','p','g2'] # 1 = prize, 2 and 3 are goat
ch = shuffle(ch)  # shuffle the list [g,p,g]

correct_ans = ch.index('p')  # gets the index of p from shuffled list
fg = ch.index('g1')
sg = ch.index('g2')

user = eval(input('Enter a choice from 1 to 3: ')) # 0, 1, 2
user -= 1
flag = False

if user == correct_ans:
    rm = choice([sg,fg])

    if rm == sg: 
        other = fg # 2
    else: 
        other = sg 

    q = input('Do you wish to change your choice? ')
    if q.lower() == 'yes':
        user = other

    if user == correct_ans:
        flag = True

elif user == sg:
    rm = fg
    other = correct_ans

    q = input('Do you wish to change your choice? ')
    if q.lower() == 'yes':
        user = correct_ans

    if user == correct_ans:
        flag = True

elif user == fg:
    rm = sg
    other = correct_ans

    q = input('Do you wish to change your choice? ')

    if q.lower() == 'yes':
        user = correct_ans

    if user == correct_ans:
        flag = True


if flag:
    print('Got the answer')


'''
# EXERCISE 5.9
# 14
'''
import random

def monty_hall_simulation(num_simulations, num_doors):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_simulations):
        # Place the prize randomly behind one of the doors
        prize_door = random.randint(1, num_doors)

        # Contestant makes an initial choice
        contestant_choice = random.randint(1, num_doors)

        # Monty opens one door that doesn't contain the prize
        doors_opened = [door for door in range(1, num_doors + 1) if door != contestant_choice and door != prize_door]
        monty_opens = random.choice(doors_opened)

        # Contestant decides whether to switch or stay
        remaining_doors = [door for door in range(1, num_doors + 1) if door != monty_opens]
        switch_choice = [door for door in remaining_doors if door != contestant_choice][0]

        # Check if contestant wins based on switch or stay
        if contestant_choice == prize_door:
            stay_wins += 1
        elif switch_choice == prize_door:
            switch_wins += 1

    stay_percentage = (stay_wins / num_simulations) * 100
    switch_percentage = (switch_wins / num_simulations) * 100

    return stay_percentage, switch_percentage

def main():
    num_simulations = 10000

    # Simulate Monty Hall problem with three doors
    stay_percentage, switch_percentage = monty_hall_simulation(num_simulations, 3)
    print(f"With three doors:")
    print(f"Percentage of wins by staying: {stay_percentage:.2f}%")
    print(f"Percentage of wins by switching: {switch_percentage:.2f}%\n")

    # Simulate Monty Hall problem with four doors
    stay_percentage, switch_percentage = monty_hall_simulation(num_simulations, 4)
    print(f"With four doors:")
    print(f"Percentage of wins by staying: {stay_percentage:.2f}%")
    print(f"Percentage of wins by switching: {switch_percentage:.2f}%")

if __name__ == "__main__":
    main()

'''
# Question:
