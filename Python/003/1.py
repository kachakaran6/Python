# Numbers, Type Conversion and Mathematics

# numeric dat type

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 6.9
print(num2, 'is of type', type(num2))

num3 = 5+2j
print(num3, 'is of type', type(num3))

print('----------------------------------------------------------')

# -------------------------------------------------------------------

# Number system

print('This is an example of Binary : ',0b1101011)     #binary

print('This is an example of Octal : ',0xFB + 0b10 )

print('This is an example of Hexadecimal :', 0o15)

print('----------------------------------------------------------')

# --------------------------------------------------------------------

# Random Module

import random

print(random.randrange(10,100))   #prints random number between given range

print(int(random.random()*100))

list1 = ['a', 'b', 'c', 'd', 'e']
# get random item from list1
print(random.choice(list1))

# shuffle the list elements
random.shuffle(list1)
print(list1)

print('----------------------------------------------------------')

# --------------------------------------------------------------------

# Math Module

import math

print('Pi value',math.pi)
print('Get Square Root',math.sqrt(9))
print('Get Power',math.pow(2,3))
print(math.ceil(3.7))
print(math.floor(3.7))
print('Factorial of number 5 : ',math.factorial(5))


