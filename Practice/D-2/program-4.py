#Right Triangle Start Pattern

size = int(input('Enter a number: '))

for i in range(size):
    for j in range(size - i - 1):
        print('  ', end='')
    for j in range(i + 1):
        print('* ', end='')
    print()
    