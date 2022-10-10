'''
Q24. Write a Python program to get the size of an object in bytes.
'''

import sys

object = 'object'

print(f'Size of this object is : {str(sys.getsizeof(object))} bytes')