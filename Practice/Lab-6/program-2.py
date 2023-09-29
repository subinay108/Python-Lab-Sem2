# Magic Square

n = int(input('Enter no. of grids: '))

def pprint(arr):
    s = len(str(n * n))
    for i in arr:
        for j in i:
            print(f'%{s}d'%j, end = '  ')
        print()

def oddOrderSolve():
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

def doublyEvenOrderSolve():
    # fill the square with 1 to n*n
    i = 1
    for row in range(n):
        for col in range(n):
            square[row][col] = i
            i += 1
    # change the corners
    square[0][0], square[n-1][n-1] = square[n-1][n-1], square[0][0]
    square[0][n-1], square[n-1][0] = square[n-1][0], square[0][n-1]
    
    # change the center square
    square[n//2 - 1][n//2 - 1], square[n//2][n//2] = square[n//2][n//2], square[n//2 - 1][n//2 - 1]
    square[n//2 - 1][n//2], square[n//2][n//2 - 1] = square[n//2][n//2 - 1], square[n//2 - 1][n//2]
    

def singlyEvenOrderSolve():
    pass

# Fill the square with 0
square = []
for i in range(n):
    square.append([0] * n)

if n % 2 != 0: # odd order
    oddOrderSolve()
elif n % 4 == 0: # Doubly even order
    doublyEvenOrderSolve()
else: # Singly even order
    singlyEvenOrderSolve()

pprint(square)