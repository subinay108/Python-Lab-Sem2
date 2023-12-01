# Date: 01/12/2023
# If a positive integer is entered through the keyboard, write a recursive function to obtain the prime
# factors of the number

def getPrimeFactors(n, count = 2):
    if n <= 1:
        return 
    elif n % count == 0:
        print(count, end = ' ')
        getPrimeFactors(n // count)
    else:
        getPrimeFactors(n, count + 1)

    

n = int(input('Enter a positive integer: '))

print(f'Prime Factors of {n}:', end=' ')
getPrimeFactors(n)

