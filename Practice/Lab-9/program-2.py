# Perform the following operation on the list of Numbers
# - Create a list of 5 odd numbers
# - Create a list of 5 even numbers
# - Combine the two lists
# - Add prime numbers 11, 17, 29 at the beginning of the combined list
# - Report how many elements are present in the list
# - Replace last  3 numbers in the list with 100, 200, 300
# - Delete all the numbers in the list
# - Delete the list

l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]

l = l1 + l2

l = [11, 17, 29] + l
print(l)

print(len(l))

l = l[:-3] + [100, 200, 300]
print(l)

l.clear()

del l
