# WAP for factorial of a number
n = int(input('Enter a number: '))

fact = 1
for i in range(n, 1, -1):
    fact *= i

print(f'Factorial of {n} : {fact}')