#!/usr/bin/env python3

# we need to import sys to access command-line arguments for python script
import sys

'''
print(sys.version) # tells us the version of the python currently in use
print(sys.platform) # tells us our operating system platform
print(sys.argv) # tells us a list of all items given at the command line when running our python script from a command shell
print(len(sys.argv)) # tells us the number of command line arguments the user provide from a command shell
sys.exit() # will immediately end the running Python script, ignoring the remaining lines in the Python script
'''

'''
3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0]
linux
['./showargs.py']
1
'''
arguments = sys.argv
name = sys.argv[0]

print('Print out ALL script arguments: ', arguments)
print('Print out the script name: ' + name)
print('Print out the number of argument: ', len(sys.argv))

'''
jkuang11@jkuang11:~/ops445/lab2$ ./showargs.py
Print out ALL script arguments:  ['./showargs.py']
Print out the script name: ./showargs.py
Print out the number of argument:  1
jkuang11@jkuang11:~/ops445/lab2$ ./showargs.py testing different arguments
Print out ALL script arguments:  ['./showargs.py', 'testing', 'different', 'arguments']
Print out the script name: ./showargs.py
Print out the number of argument:  4
jkuang11@jkuang11:~/ops445/lab2$ ./showargs.py argument1 argument2 argument3 argument4
Print out ALL script arguments:  ['./showargs.py', 'argument1', 'argument2', 'argument3', 'argument4']
Print out the script name: ./showargs.py
Print out the number of argument:  5
jkuang11@jkuang11:~/ops445/lab2$

'''
