'''
Q22. Write a Python program to get the command-line arguments (name of the script, the number
of arguments, arguments) passed to a script.
'''
import sys
 
n = len(sys.argv)
print("Total arguments passed:", n)
 
print("Name of Python script:", sys.argv[0])
 
print("Arguments passed: ")
for i in range(1, n):
    print(sys.argv[i])