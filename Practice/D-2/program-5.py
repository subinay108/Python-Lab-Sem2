#left downward triangle pattern

size = int(input('Enter a number: '))

for i in range(size):
    for j in range(size - i):
        print('* ', end='')
    print()
    