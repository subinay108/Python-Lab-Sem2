# Print all factorial values & squared of a given list of values using map() function
from math import factorial

l = list(map(int, input('Enter a list of numbers: ').split()))

# factorial values
print(list(map(factorial, l)))

# squared values
print(list(map(lambda x: x * x, l)))