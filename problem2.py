#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

import math
print("\n\n     Enter a number")
x = input()
x = float(x)
y = round(x,0)

if (x == y):
    print("this number is an integer")
    input()
else:
    print("this is not an integer")
    input()

    