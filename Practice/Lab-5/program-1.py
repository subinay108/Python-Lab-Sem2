# WAP to find pair prime number 
l = int(input('Enter lower limit: '))
u = int(input('Enter upper limit: '))

def isPrime(n):
    if n < 2:
        return False
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    return prime

for i in range(l, u - 1):
    if isPrime(i) and isPrime(i + 2):
        print(i, ',', i + 2)

