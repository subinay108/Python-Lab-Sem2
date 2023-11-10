# Wrtie a program to create three dictionaries and concatenate them to create fourth dictionary

d1 = {1: 'a', 2: 'b'}
d2 = {'a': 1, 'b': 2}
d3 = {'Name': 'Subinay'}

d4 = {**d1, **d2, **d3}

print(d4)
