#Right Pascal Star Pattern

size = int(input('Enter a number: '))

for i in range(size):
    for j in range(i + 1):
        print('* ', end='')
    print()

for i in range(size):
    if not i:
        continue
    for j in range(size - i):
        print('* ', end='')
    print()