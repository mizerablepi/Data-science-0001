'''
Q9. Write a Python program to concatenate all elements in a list into a string and return it.
'''

list = [1,'a',24,'rt',222,34]
output = ''.join(map(str, list))
print(output)