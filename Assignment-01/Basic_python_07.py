'''
Q7. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

array = [1, 5, 8, 3]
print("Enter a number to check: ")

input = int(input())

print(True if input in array else False)