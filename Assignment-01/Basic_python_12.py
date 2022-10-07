'''
12. Write a python program to call an external command in Python.
'''

from subprocess import call
print('Enter command to run: ')
cmd = [x for x in input().split(' ')]

call(cmd)