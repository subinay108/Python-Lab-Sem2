#pyramid pattern

size = int(input('Enter a number: '))

for i in range(size):
    for j in range(size - i - 1):
        print('  ', end='')
    for j in range(i * 2 + 1):
        print('* ', end='')
    for j in range(size - i - 1):
        print('  ', end='')
    print()
    