#!/usr/bin/env python3

# Author: Joanne Kuang
# Date: 09-23-2024
# Program: lab2d.py
'''
Input / Output Requirements

The script should have a Shebang line
The script should import sys
The script should print a usage message if zero arguments present, or if not exactly 2 arguments are provided when running the script (NOTE: Use sys.argv[0] value in this message in case you rename the script at a later date!)
The script should exit without attempting to do any more work if exactly 2 arguments are not provided when running script
The script should use an object called name
The script should use an object called age
The script should assign the string sys.argv[1] (first argument) to the object "name"
The script should assign the string sys.argv[2] (second argument) to the object "age"
The script should print the EXACT OUTPUT as show
'''
import sys # we need to import the sys  module so we can access it in our python script

# 1. checks if there is zero arugments entered
if len(sys.argv) < 3:
    print('Usage: ' + sys.argv[0] + ' name age')
    sys.exit()

# 2. Check if there are more than 2 arguments
if len(sys.argv) > 3:
    print('Usage: ' + sys.argv[0] + ' name age')
    sys.exit()

# we must add command-line arguments to python script
name = sys.argv[1]  # before we used (name)
age = sys.argv[2]   # before we used (age)

print('Hi ' + name + ', you are ' + str(age) + ' years old.')


