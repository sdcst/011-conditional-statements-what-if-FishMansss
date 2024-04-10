#! python3 

"""
Have the user enter a number. 
Use an if...elif statement to determine if the number is 
a) larger than 1000 
b) larger than 100 
c) larger than 10 
d) larger than 0 
Output must match one of the valid output statements listed
(2 points)

Inputs:
a number

Output is a single number that represents a range of numbers:
"3" : The number is equal to 1000 or is larger than 1000
"2" : The number is 100 or a number up to 1000 
"1" : The number is 10 or a number up to 100 
"0" : The number is 0 or a number up to 100 

Example:
Enter a number: 3
0

Enter a number: 212
2

Enter a number: 10000
3


"""
import math
import os 

print("\n\n     Enter a positive number")
x = input()
x = int(x)
os.system('cls')


if (10 < x < 101):
    print("\n   1")
    input()
if (0 < x < 101 ):
    print("\n   0")
    input()
if (100 < x < 1001):
    print("\n   2")
    input()
if (x > 1000):
    print("\n   3")
    input()
if (x < 0): 
    print("that is not positive")
