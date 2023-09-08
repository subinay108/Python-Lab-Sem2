# WAPP to generate and print a list when elements are received from keyboard

n = int(input('Enter the no. of elements to input: '))

x = []
for i in range(n):
    element = int(input(f'Enter element {i + 1}: '))
    x.append(element)

print('The list is:', x)
print('Maximum element in the list:', max(x))
print('Minimum element in the list:', min(x))
print('Sum of all the elements is:', sum(x))
print('Average of all the elements is:', )
