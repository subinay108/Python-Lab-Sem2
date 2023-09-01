# Date: 18-08-2023
# Program -2 : Write a python program to print all even and odd natural no. within a lower and upper limit

l = int(input('Enter the lower limit: '))
u = int(input('Enter the upper limit: '))

print('Even numbers are: ', end='')
for i in range(l, u + 1):
    if i % 2 == 0:
        print(i, end=' ')

print('\nOdd numbers are: ', end='')
for i in range(l, u + 1):
    if i % 2 != 0:
        print(i, end=' ')