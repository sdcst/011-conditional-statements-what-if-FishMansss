#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math
import os

print("\n\n     Enter side 'a'")
a = input()
a = float(a)
print("\n       Enter side 'b'")
b = input()
b = float(b)
print("\n       Enter side 'c'")
c = input()
c = float(c)
os.system('cls')
if (a == b == c):
    print("equilateral")
    input()
if (a>b>c):
    l = a
    hyp = (b**2 + c**2)**.5
if (a>c>b):
    l = a
    hyp = (b**2 + c**2)**.5
if (b>a>c):
    l = b
    hyp = (a**2 + c**2)**.5
if (b>c>a):
    l = b
    hyp = (a**2 + c**2)**.5
if (c>b>a):
    l = c
    hyp = (a**2 + b**2)**.5
if (c>a>b):
    l = c
    hyp = (a**2 + b**2)**.5
os.system('cls')

if (l + l *.02 )
##where i left off


'''
if (hyp > a + a * 0.2):
    print("obtuse")
if (hyp < a - a * 0.2):
    print("accute")
if (hyp > b + b * 0.2):
    print("obtuse")
if (hyp < b - b * 0.2):
    print("accute")
if (hyp > c + c * 0.2):
    print("obtuse")
if (hyp < c - c * 0.2):
    print("accute")
if (hyp ):
'''

print(f"your triangle is {hyp}")
input()
