# Date: 18-08-2023
# Program -3 : Write a python program to check whether an integer number is prime or not

n = int(input('Enter an integer number: '))

prime = True

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        prime = False
        break

if n > 1 and  prime:
    print(n, 'is Prime')
else:
    print(n, 'is Not Prime')