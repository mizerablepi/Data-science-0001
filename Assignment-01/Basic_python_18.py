'''
Q18. Write a Python program to get an absolute file path
'''
import os

print("Enter file name: ")
file = input()
print(os.path.abspath(file))   
