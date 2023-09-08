# WAPP to sort elements of list in asscending order
# using built-in functions
# without using built-in functions

l = [10, 25, 7, 30, 15]
# l.sort()

for i in range(len(l)):
    for j in range(len(l) - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
        


print('The list in sorted order:', l)