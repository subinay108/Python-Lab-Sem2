# A positive integer is entered through the keyboard, write a recursive function to calculate sum of
# digits of the 5-digit number

def sumOfDigits(n):
    if n == 0:
        return 0
    return (n % 10) + sumOfDigits(n//10)

n = int(input('Enter a positive integer: '))

print(f'The sum of the digtis of {n}: {sumOfDigits(n)}')