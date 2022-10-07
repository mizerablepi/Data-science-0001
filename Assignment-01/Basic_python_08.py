'''
Q8. Write a Python program to create a histogram from a given list of integers.
'''

array = [int(x.strip()) for x in input().split(',')]

for i in array:
    print(f'{i}','*' * i)