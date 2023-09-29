# WAP to check the greatest number among three

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

big = a
if big < b:
    big = b
if big < c:
    big = c

print(f'Greatest number is {big}')