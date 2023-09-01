# WAP to find sum of all digits of the numbers appearing within a given range of natural numbers

l = int(input('Enter lower limit: '))
u = int(input('Enter upper limit: '))

for n in range(l, u + 1):
    temp_n = n
    if n < 0:
        n = -n

    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    
    # print(f'Sum of digits of {temp_n} is = {s}')
    print('Sum of digits of %d is = %d'%(temp_n, s))