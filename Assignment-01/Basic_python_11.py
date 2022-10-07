'''
11. Write a Python program to check whether a file exists.
'''

from ast import IfExp
import os
 
print("Enter path to check : ")
path = input()

isExist = os.path.exists(path)
if isExist:
    print('File exists')
else:
    print("File doesn't exist")