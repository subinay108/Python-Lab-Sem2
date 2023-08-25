# Date: 18-08-2023
# Program -4 : Write a python program to print all the prime no. within a lower and upper limit

l = int(input('Enter the lower limit: '))
u = int(input('Enter the upper limit: '))

for n in range(l, u + 1):
    prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if n > 1 and  prime:
        print(n, end = ' ')