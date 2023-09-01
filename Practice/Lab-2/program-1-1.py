#Rectangle Pattern in Python
row = int(input('Enter rows: '))
col = int(input('Enter cols: '))


# for i in range(row):
#     for j in range(col):
#         print('* ', end='')
#     print()

#alternate
print(('* ' * col + '\n') * row)

