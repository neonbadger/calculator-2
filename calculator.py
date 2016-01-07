"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    input = raw_input()

    token = input.split(" ")

    if "q" in token:
        print "Had enough? Okay."
        break
    elif len(token) <= 2:
        print "Sorry, you need more than one number to do that."
        continue 
    elif len(token) >= 3:
        
        if len(token) > 3:
            print "we will perform operation on the first 2 numbers from your input."
        
        try:
            num1 = float(token[1])
            num2 = float(token[2])
        except ValueError:
            print "Please put in valid numbers to perform calculations."
            continue

        if token[0] == "+":
            print add(num1, num2)
        elif token[0] == "-":
            print subtract(num1, num2)
        elif token[0] == "*":
            print multiply(num1, num2)
        elif token[0] == "/":
            print divide(num1, num2)
        elif token[0] == "square":
            print square(num1)
        elif token[0] == "cube":
            print cube(num1)
        elif token[0] == "pow":
            print power(num1, num2)
        elif token[0] == "mod":
            print mod(num1, num2)



# Your code goes here

    