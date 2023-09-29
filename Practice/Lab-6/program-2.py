# Magic Square

n = int(input('Enter no. of grids: '))

def pprint(arr):
    s = len(str(n * n))
    for i in arr:
        for j in i:
            print(f'%{s}d'%j, end = '  ')
        print()

def oddOrderSolve(r_offset, c_offset, start, n):
    row =  n // 2
    col =  n - 1

    for i in range(start, n * n + start):
        square[r_offset * n + row][c_offset * n + col] = i
        temp_row = row
        temp_col = col
        row = (row + 1) % n
        col = (col + 1) % n
        if square[r_offset * n + row][c_offset * n + col]:
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
    # divide the square into four parts and solve odd order
    oddOrderSolve(0, 0, 1, n // 2)
    oddOrderSolve(1, 1, 10,  n // 2)
    oddOrderSolve(0, 1, 19, n // 2)
    oddOrderSolve(1, 0, 28, n // 2)
    

# Fill the square with 0
square = []
for i in range(n):
    square.append([0] * n)

if n % 2 != 0: # odd order
    oddOrderSolve(0, 0, 1, n)
elif n % 4 == 0: # Doubly even order
    doublyEvenOrderSolve()
else: # Singly even order
    singlyEvenOrderSolve()

pprint(square)