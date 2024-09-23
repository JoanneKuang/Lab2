#!/usr/bin/env python3

# Author: Joanne Kuang
# Student ID: 165994187
# Date: 2024-09-23
# Program: lab2g.py

'''
Input / Output / Processing Requirements
The script should have a Shebang line
The script should have a comment line which contains the word "Author:" and your full name
The script should have another comment line which contains the word "Author ID:" and your seneca_id
The script should have another comment line which contains the word "Date Created:" and the actual date in "yyyy/mm/dd" format
The script should import sys
The script should assign the value of 3 to an object named timer when there is no arguments provided.
The script should assign the value of int(sys.argv[1]) if an object named timer when one command line argument (sys.argv[1]) are entered
The script should have a WHILE loop that repeats until (and not including when) timer equals 0
The script should print the EXACT OUTPUT as shown
'''
import sys

timer = 3 # set timer 3 when there is no arguement provided

# if arguement is more than 1 then do below
if len(sys.argv) > 1:
# this will take whatever number and count down
	timer = int(sys.argv[1]) # before named count change to timer

# this will count down
while timer > 0:
	print(timer)
	timer = timer - 1
print('blast off!')
