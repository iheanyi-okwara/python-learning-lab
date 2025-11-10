# EXERCISE 5.9
# 1
'''
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.

count = 0
for i in range(1, 101):
    if (i**2)% 10==1:
        count=count+1
print(count)
'''

# 2
'''
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
4 and how many end in a 9.

count = 0
count2 = 0
for i in range(1, 101):
    if (i**2)% 10==4:
        count=count+1
    if (i**2)% 10==9:
        count2=count2+1
print('Number of squares ending in 4: ', count)
print('Number of squares ending in 9: ', count2)
'''

# 3 Revisit
'''
Write a program that asks the user to enter a value n, and then computes (1+1/2 +1/3 +···+1/n)−
ln(n). The ln function is log in the math module.
'''


# 4
'''
Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000

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
