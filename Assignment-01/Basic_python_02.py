"""
Q2. Write a Python program which accepts a sequence of comma-separated numbers from the
user and generates a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

# TODO
print('Enter a sequence of numbers seperated by comma: ')

input = input().split(',')
input = [x.strip() for x in input]

print(input)