#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""

import math
import os 
print("\n\n     Enter a number:", end=" ")
num = input()
num = int(num)

if (num > 0):
    os.system('cls')
    print("\n   your number is positive")
    input()

if (num < 0):
    os.system('cls')
    print("\n   your number is negative")
    input()

else:
    print("\n   your number is zero")
    input()