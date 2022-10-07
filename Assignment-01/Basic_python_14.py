'''
Q14. Write a Python program to list all files in a directory in Python.
'''
from subprocess import call

print('Enter directory: ')
dir = input()

call(['ls','-a',dir])