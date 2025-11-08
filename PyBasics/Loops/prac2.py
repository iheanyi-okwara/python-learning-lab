# CHAPTER 2: EXERCISE 2.5    (SAT/08/11/2025)
# print('1.','Write a program that prints your name 100 times.')
# for i in range(100):
#     print('Henry')

# print('2.','Write a program to fill the screen horizontally and vertically with your name.')
# for i in range(5):
#     print('Henry'*(i+1), end=' ')
# for i in range(5):
#     print('Henry')

# print('3.','Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it.')
# for i in range(10):
#     print(i+1, 'Henry')

# print('4.','Write a program that prints out a list of the integers from 1 to 20 and their squares.')
# for i in range(1,21):
#     print(i,'---',(i*i))

# print('5.','Write a program that uses a for loop to print the numbers 8,11,14,17,20,...,83,86,89.')
# for i in range(8,92,3):
#     print(i, end=' ')

# print('6.','Write a program that uses a for loop to print the numbers 100,98,96,...,4,2.')
# for i in range(100,0,-2):
#    print(i, end=' ')

# print('7.','Write a program that uses exactly four for loops to print the sequence of letters below.')
# for i in range(10):
#     print('A')
# for i in range(7):
#     print('B')
# for i in range(4):
#     print('C')
#     print('D')
# print('E')
# for i in range(6):
#     print('F')
# print('G')

# print('8.','Write a program that asks the user for their name and how many times to print it. The program should print out the users name the specified number of times.')
# for i in range(5):
#     num1 = eval(input('Enter your name:'))
#     num = eval(input('How many times should your name be printed:'))
#     print(i+1, num1*num)
# print('The loop is now done.')

# REVISIT THIS QUESTION:
# print('9.','Write a program that asks the user how many Fibonacci numbers to print and then print that many.')
# for i in range(3):
#     num = eval(input('Enter how many Fibonacci numbers to print:'))
#     print(i, num+num, end=' ')

'''
#correction
def generate_fibonacci(n):
    fibonacci_sequence = [1, 1]
    for _ in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

def main():
    try:
        num_of_terms = int(input("Enter the number of Fibonacci numbers to print: "))
        if num_of_terms <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_numbers = generate_fibonacci(num_of_terms)
            print(f"The first {num_of_terms} Fibonacci numbers are: {fibonacci_numbers}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()

'''

# 10.
# for i in range(4):
#     print('*'*10)

# 11.
# for i in range(4):
#    num = eval(input('Enter how wide you want it:'))
#    print('*'*num, sep='')

# 15
# height = input('How high do you want your A?')
# height = eval(height)

# print(' ' * height, '*', sep='')

# for i in range(1, height):
#     if i == height // 2:
#         print(' ' * (height - i), '*', '*' * (2 * i - 1), '*', sep='')
#     else:
#         print(' ' * (height -i), '*', ' ' * (2 * i -1), '*', sep='')
