#! python3

"""
Have the user input a number. 
Determine if the number is larger than 100 
If it is, the output should read "The number is larger than 100" 
(2 points)
Inputs:
number
Outputs:
"The number is larger than 100"
"The number is smaller than 100"
"The number is 100"

Example:
Enter a number: 100
The number is 100

Enter a number: 102
The number is larger than 100
"""
import math
import os
print("\n\n     Enter primary number")
x = input()
x = int(x)


os.system('cls')
if (x > 100):
    print(f"\n{x} is greater than 100")
    input()

if (x < 100):
    print(f"\n{y} is less than 100")
    input()