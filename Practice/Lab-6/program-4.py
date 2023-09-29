# WAP to check the number is armstrong or not

n = int(input('Enter a number: '))

def countDigit(n):
    count = 0
    while n:
        n //= 10
        count += 1
    return count

def isArmStrong(n):
    original_n = n
    s = 0
    p = countDigit(n)
    while n:
        digit = n % 10
        s += digit ** p 
        n = n // 10
    
    return (s == original_n)
    

if isArmStrong(n):
    print(f'{n} is armstrong')
else:
    print(f'{n} is not armstrong')

# for i in range(1, 10000):
#     if isArmStrong(i):
#         print(i)