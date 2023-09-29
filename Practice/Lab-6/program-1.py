# 29.09.2023
# Inverted Up Arrow Character Pattern

n = int(input('Enter a number: '))

# First line
for i in range(n - 1):
    print(chr(65 + i) + ' ', end = '')

for i in range(n - 1, -1, -1):
    print(chr(65 + i) + ' ', end = '')

print()

# Other lines
for j in range(n - 2, -1, -1):
    # Right Characters
    for i in range(j + 1):
        print(chr(65 + i) + ' ', end = '')
    
    # Middle Spaces
    for i in range(2 * (n - 1 - j) - 1):
        print('  ', end = '')

    # Left Characters
    for i in range(j, -1, -1):
        print(chr(65 + i) + ' ', end = '')
    
    print()