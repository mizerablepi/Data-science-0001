'''
Q6. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

from datetime import date
 
input_1 = [int(x.strip()) for x in input().split(',')]
input_2 = [int(x.strip()) for x in input().split(',')]

date1 = date(input_1[0],input_1[1], input_1[2])
date2 = date(input_2[0], input_2[1], input_2[2])
print(f'Difference in days: {(date2-date1).days} days')