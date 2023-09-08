# WAPP to find the sum total of all the elements
n = int(input('Enter the no. of elements to input: '))

x = []
for i in range(n):
    element = int(input(f'Enter element {i + 1}: '))
    x.append(element)

sumTotal = 0
for i in x:
    sumTotal += i
print("Sum of the elements is:", sumTotal)