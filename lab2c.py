#!/usr/bin/env python3

# Author: Joanne Kuang
# Date: 09-23-2024
# Program: lab2c.py

'''
Input / Output Requirements

The script should have a Shebang line
The script should contain import sys
The script should use a string object called name
The script should use an integer object called age
The script should use sys.argv[1] (first argument) and assign it to the string object named name
The script should use sys.argv[2] (second argument) and assign it to the integer object named age
The script should print the EXACT OUTPUT as shown (including case sensitivity)

'''
import sys # we need to import the sys  module so we can access it in our python script
name = sys.argv[1] # instead of input("Name: ")
age = int(sys.argv[2]) # instead of input("Age: ") arguement converted to an int
print('Hi ' + name + ', you are ' + str(age) + ' years old.')
