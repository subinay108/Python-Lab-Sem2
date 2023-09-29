# Magic Square

n = int(input('Enter no. of grids: '))

def pprint(arr):
    for i in arr:
        for j in i:
            print(j, end = '  ')
        print()

# Fill the square with 0
square = []
for i in range(n):
    square.append([0] * n)

if n % 2 != 0: # odd order
    pass
else:
    if n % 4 == 0: # Doubly even order
        pass
    else: # Singly even order
        pass



row = n // 2
col = n - 1

for i in range(1, n * n + 1):
    square[row][col] = i
    temp_row = row
    temp_col = col
    row = (row + 1) % n
    col = (col + 1) % n
    if square[row][col]:
        row = temp_row
        col = temp_col - 1

pprint(square)