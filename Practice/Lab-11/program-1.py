# Date: 24/11/2023
# WAP to receive three integers from keyboard and get their sum and product calculated through a 
# user-defined function cal_sum_prod()

a = int(input('Enter first integer: '))
b = int(input('Enter second integer: '))
c = int(input('Enter third integer: '))

def cal_sum_prod(a, b, c):
    return (a + b + c, a * b * c)

sum, prod = cal_sum_prod(a, b, c)

print('Sum:', sum, 'Product:', prod)