# Date: 10/11/2023
# Write a program to carry out the following operations on the given set
# s = {10, 2, -3, 4, 5, 88}
# - numbers of items in set s
# - maximum elements in set s
# - minimum elements in set s
# - sum of all elements in set s
# - obtain a new sorted set from s, set s remaining unchanged
# - report whether 100 is an element of set s
# - report whether -3 is an element of set s

s = {10, 2, -3, 4, 5, 88}

print('Number of elements:', len(s))

print('Maximum element in set s:', max(s))

print('Minimum element in set s:', min(s))

print('Sum of all elements in set s:', sum(s))

print('Sorted set:', sorted(s))

print('Is 100 in set s:', 'Yes' if 100 in s else 'No')

print('Is -3 an element of s:' 'Yes' if -3 in s else 'No')