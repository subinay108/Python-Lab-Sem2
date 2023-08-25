#Diamond star pattern

size = int(input('Enter a number: '))

for i in range(size):
    for j in range(size - i - 1):
        print('  ', end='')
    for j in range(i * 2 + 1):
        if(j == 0 or j == i * 2):
            print('* ', end='')
        else:
            print('  ', end='')
    for j in range(size - i - 1):
        print('  ', end='')
    print()
    
for i in range(1, size):
    for j in range(i):
        print('  ', end='')
    for j in range((size - i) * 2 - 1):
        if(j == 0 or j == (size - i - 1) * 2):
            print('* ', end='')
        else:
            print('  ', end='')
    for j in range(i):
        print('  ', end='')
    print()
    