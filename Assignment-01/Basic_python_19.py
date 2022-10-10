'''
Q19. Write a Python program to get file creation and modification date/times.
'''

import os
import time

print("Enter the path of file: ")
path = input()

ti_c = os.path.getctime(path)
ti_m = os.path.getmtime(path)
 
c_ti = time.ctime(ti_c)
m_ti = time.ctime(ti_m)
 
print(f"The file located at the path {path} was created at {c_ti} and was last modified at {m_ti}")