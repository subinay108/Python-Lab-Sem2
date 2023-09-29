# WAP for n-th fibonacci series

n = int(input('Enter n: '))

a = b = 1
for i in range(n):
    print(a, end = ' ')
    a, b = b, a + b 

