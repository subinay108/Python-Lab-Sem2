# WAP to find the armstrong numbers

def getNoOfDigits(n):
    count = 0
    while(n > 0):
        count += 1
        n //= 10
    return count

def isArmStrong(n):
    original_n = n
    s = 0
    p = getNoOfDigits(n)
    while(n > 0):
        d = n % 10
        s += d ** p
        n //= 10
    
    return s == original_n
    
lb = int(input('Enter lower bound: '))
ub = int(input('Enter upper bound: '))

for i in range(lb, ub + 1):
    if isArmStrong(i):
        print(i)