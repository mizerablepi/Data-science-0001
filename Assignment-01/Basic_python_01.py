#Q1. Write a Python program which accepts the user's first and last name and prints them in reverse order with a space between them.

print('Enter First name')
f_name = input()

print('Enter Last Name')
l_name = input()

print('Your name reversed')
print(f_name[::-1], l_name[::-1])
