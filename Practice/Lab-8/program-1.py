# Date: 13/10/2023
# Write a program that receives 3 sets of values of p, n and  r and calculates simple interest for each
for i in range(3):
    print(f'Set-{i + 1}')
    p = float(input('Enter principle: '))
    n = int(input('Enter time period: '))
    r = float(input('Enter rate of interest: '))
    simpleInterest = p * n * r / 100
    print('Simple interest:', simpleInterest)