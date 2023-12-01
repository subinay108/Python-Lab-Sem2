# If a positive integer is entered through the keyboard, write a recursive function to obtain the prime
# factors of the number

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def getPrimeFactors(n):
    for i in range(2, n + 1):
        if isPrime(i):
            if n % i == 0:
                print(i, end=' ')
                getPrimeFactors(n//i)
                break

    

n = int(input('Enter a positive integer: '))

print(f'Prime Factors of {n}:', end=' ')
getPrimeFactors(n)

