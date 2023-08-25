#hollow triangle start pattern

size = int(input('Enter a number: '))

for i in range(size):
    for j in range(i + 1):
        if(i == size - 1 or j == 0 or j == i):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
    