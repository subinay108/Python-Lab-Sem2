# WAP to print the sum total of all even and odd natural numbers separately
# upto a limit

n = int(input('Enter the limit: '))

i = 1
evenSum = oddSum = 0
while i <= n:
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
    i += 1

print(f'Sum of even numbers upto {n}: {evenSum}')
print(f'Sum of odd numbers upto {n}: {oddSum} ')