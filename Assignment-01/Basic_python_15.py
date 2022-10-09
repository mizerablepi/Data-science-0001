'''
Q15. Write a python program to access environment variables.
'''
import os

print("Enter the environment variable to view: ")
var = input()
print(os.environ[var])