#Hollow Square Pattern in Python

size = int(input('Enter a number: '))

# for i in range(size):
#     for j in range(size):
#         if(i == 0 or j == 0 or i == size - 1 or j == size - 1):
#             print('* ', end='')
#         else:
#             print('  ', end='')
#     print()

# alternate
print('* ' * size )
print(('* ' + '  ' * (size - 2) + '*\n') * (size - 2), end='')
print('* ' * size )
