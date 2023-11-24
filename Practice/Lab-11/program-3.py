# Write a function to create and return a list containing tuples of the form (x, x^2, x^3) for 
# all x between 1 and 20(both included)

def func():
    return list(map(lambda x: (x, x**2, x**3), list(range(1, 21))))


List = func()

for i in List:
    print(i)