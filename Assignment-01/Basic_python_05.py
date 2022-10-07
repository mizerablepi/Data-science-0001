'''
Q5. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''

# importing the calendar module
import calendar

print("Enter Year")
year = int(input())
print("Enter month")
month = int(input())
print(calendar.month(year, month))