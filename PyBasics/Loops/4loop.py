# CHAPTER 2: FOR LOOPS           (SAT/08/11/2025)
# For loops
# print('*****************')
# print('*****************')
# print('*****************')
# print('*****************')

# for i in range(20,0,-1):
#     print(i)

# for i in range(10):
#     print('Hello')

# for i in range(3):
#     num = eval(input('Enter a number:'))
#     print('The square of your number is', num*num)
# print('The loop is now done')

# print('A')
# print('B')
# for i in range(5):
#     print('C')
#     print('D')
# print('E')

# print('A')
# print('B')
# for i in range(5):
#     print('C')
# for i in range(5):
#     print('D')
# print('E')

# for i in range(100):
#     print(i)

# for i in range(3):
#     print(i+1, '---Hello')

# for i in range(10):
#     print(i)
# for i in range(1,10):
#     print(i)
# for i in range(3,7):
#     print(i)
# for i in range(2,15,3):
#     print(i)
# for i in range(9,2,-1):
#     print(i)

# for i in range(5,0,-1):
#     print(i, end=' ')
# print('Blast off!!!')

# for i in range(4):
#     print('*'*6)

# for i in range(4):
#     print('*'*(i+1))

# for i in range(20,0,-1):
#     print('A'*i)
#     print(i, end=' ')

# h = eval(input(' what is the height ' ))
# for i in range(h):
#     print(' '*(h-i),'*'*((2*i)+1),sep='')
# for i in range(h-2, -1, -1):
#     print(' '*(h-i),'*'*((2*i)+1),sep='')

# h = eval(input(' what is the height ' ))
# for i in range(h):
#     print(' '*(h-i) + '*'*(h*2-1-2*(h-i)))


#  for i in range(size):
#         left_space = abs(size - i)
#         right_space = size * 2 - 1 - 2 * left_space
#         print(" " * left_space + "*" * right_space)


# h = eval(input(' what is the height ' ))
# for i in range(h):
#     print(' '*(h-i),'*',' *'*i,sep='')


# Get input from user
height = input('How high do you want your A?')
height = eval(height)

# print(' ' * height, '*')
# print(' ' * (height -1) , '*')
# print(' ' * (height -2) , '*')
# print(' ' * (height -3) , '*')
# print(' ' * (height -4) , '*')
# print(' ' * (height -5) , '*')

# OR
# print(' ' * height, '*', sep='')

# for i in range(1, height):
# #    print(' ' * (height -1), '*')
#     if i == height // 2:
#     # do something
#         print(' ' * (height - i), '*', '*' * (2 * i - 1), '*', sep='')
#     else:
#         print(' ' * (height -i), '*', ' ' * (2 * i -1), '*', sep='')

# print(' ' * height, '*')
# for i in range(1, height): 1, 2, 3, 4, ..., height -1

# for i in range(1, height):
#    print(' ' * (height -i), '*')

# for i in range(1, height):
#    print(' ' * (height - i), '*', ' ' * (2 * i - 1))


# n = 0, 1, 2, 3 ....
# odd numbers = 2n+1 or 2n-1

# a = 2
# b = 4
# c = 6
# print(a, b, c, sep='')


# height = input('How high do you want your A?')
# height = eval(height)

# print(' ' * height, '*', sep='')

# for i in range(1, height):
#    if i == height // 2:
# do something
#        print(' ' * (height - 1), '*', '*' * (2 * i - 1), '*', sep='')
#    else:
#        print(' ' * (height - 1), '*', ' ' * (2 * i - 1), '*', sep='')


# print(' ' * height, '*', sep='')

# for i in range(1, height):
#    print(' ' * (height - i), '*', ' ' * (2 * i - 1), '*', sep='')
# loop
# for num in range(100):
#     print(num, end=' ')

# # reverse loop
# for num in range(100,0,-5):
#     print(num,end=' ')
