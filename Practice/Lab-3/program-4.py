# WAP to find sum of all digits of an integer number received from keyboard

n = int(input('Enter an integer: '))

if n < 0:
    n = -n

s = 0
while n > 0:
    s += n % 10
    n //= 10

print('Sum of digits:', s)