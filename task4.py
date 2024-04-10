#! python3

"""
Have the user enter in a sentence. 
Check to see if the word "password" is located in the sentence

Inputs:
a sentence

Outputs:
"the sentence contains password"
"the sentence does not contain password"

Examples:
Enter a sentence: I will not buy this record, it is scratched.
the sentence does not contain password

Enter a sentence: The best password is no password.
the sentence contains password
"""
import math
import os

print("\n\n     Please enter a sentance")
p = input()
p = str(p)
os.system('cls')

if ("password" in p):
    print("the sentance contains a password")
    input()
if ("password" not in p):
    print("the sentance does not contain a password")
    input()
