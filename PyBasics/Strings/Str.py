# STRINGS
'''
A string is created by enclosing text in quotes. You can use either single quotes,
', or double quotes, ". A triple-quote can be used for multi-line strings. Here are some examples:
s = 'Hello'
t = "Hello"
m = """This is a long string that is
spread across two lines."""


st = 'string'

#Concatenation and repetition
st1 = 'My name is '
st2 = 'John'

st3 = st1 + st2
print(st3)

st4 = st2 * 10
#print(st4)

num = input('What is your age? ')

#Iterable (Indexing and in operator)
The in operator is used to tell if a string contains something. For example:
if 'a' in string:
print('Your string contains the letter a.')
You can combine in with the not operator to tell if a string does not contain something:
if ';' not in string:
print('Your string does not contain any semicolons.')


Indexing:
We will often want to pick out individual characters from a string. Python uses square brackets to
do this. The table below gives some examples of indexing the string s='Python'.

Statement   Result      Description
s[0]           P       first character of s
s[1]           y       second character of s
s[-1]          n       last character of s
s[-2]          o       second-to-last character of s
• The first character of s is s[0], not s[1]. Remember that in programming, counting usually
starts at 0, not 1.
• Negative indices count backwards from the end of the string.



# print(st2[0])
# print(st2[1])
# print(st2[2])

print(st2[1:3])   #[start,end,step]

print(str[-2])

If 'o' in st2:
    print('yes')

if 'i' not in st2:
    print('I not in string')

'''

vowels = 'aeiou'
l = 'z'
if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
    print('It is a vowel')

# strings are immutable, you cannot change them once they are created.
# For iterable you can loop it


'''
Slices:
A slice is used to pick out part of a string. It behaves like a combination of indexing and the range
function. Below we have some examples with the string s='abcdefghij'.
index: 0 1 2 3 4 5 6 7 8 9
letters: a b c d e f g h i j

Code        Result       Description
s[2:5]      cde         characters at indices 2, 3, 4
s[ :5]      abcde       first five characters
s[5: ]      fghij       characters from index 5 to the end
s[-2: ]     ij          last two characters
s[ : ]      abcdefghij  entire string
s[1:7:2]    bdf         characters from index 1 to 6, by twos
s[ : :-1]   jihgfedcba  a negative step reverses the string

'''
