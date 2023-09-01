# WAP to find factorial value of an integer no

n = int(input('Enter an integer: '))

i = fact = 1
while i <= n:
    fact *= i
    i += 1

print('Factorial of ', n, ': ', fact)