# string slicing
# string[start(inclusive), end(exclusive), stepsize(optional)]
x = 'abcdefg'
print(x[2:])
print(x[1:5]) 
print(x[0:5:2])
print(x[::-1])

# string是不可改變的
# myString1 = 'Hello'
# myString1[0] = 'h'
# print(myString1) #TypeError: 'str' object does not support item assignment

# string method
print(len(' '))

name = 'Wilson'
# object-oriented programming
# print(name.upper())
# print(name.lower())
print(name.upper().isupper()) # method chaining

name1 = 'Erin Chen'
print(name1.replace('n','c'))

sentence = 'Today is a good day.'
print(sentence.split(' '))
print(list(sentence)) # typecasting
 
# fstring
myName = 'Anne'
age = 27
print(f'Hello, I am {myName} and I am {age} years old.')