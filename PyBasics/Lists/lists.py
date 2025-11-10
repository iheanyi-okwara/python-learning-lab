'''
Python List: 
is a data structure that stores data for us
List is iterable, you can go through the items one by one
'''
'''
# Creating list
l = ['a','b','c']


s = list('string')
for i in 'aeiou':
    print(i)

s = list('string')
print(s)

# -empty list
e =[] # false, 0, ''

# - list data types
name = 'james'
d = ['a', 2, 3.2, ['a', ['i','t']], name]

#similarities to string
# - joining (concatenation) and repetition
l1 = ['a', 'b', 'c']
l2 = [1,2,3]
l3 = l1 + l2
print(l2 * 5)
'''
# CHAPTER 7: 11
result_list = []
num_ones = 2
for i in range(10):
    result_list.extend([1] + [0] * i)
    num_ones += 1

print(result_list)
