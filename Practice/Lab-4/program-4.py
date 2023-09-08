# WAPP to find the smallest element from a list

n = int(input('Enter the no. of elements to input: '))

x = []
for i in range(n):
    element = int(input(f'Enter element {i + 1}: '))
    x.append(element)

smallest = x[0]
for i in x:
    if smallest > i:
        smallest = i

print("Smallest element in the list:", smallest)