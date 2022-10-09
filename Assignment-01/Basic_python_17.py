'''
Q17. Write a program to get execution time for a Python method.
'''

from time import time


def timeit(method):
    start = time()
    method()
    end = time()

    return end - start

def test():
    for i in range(0,100):
        a = i

print(timeit(test))