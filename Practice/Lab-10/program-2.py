# Write a program to sort a dictionary in ascending/descending order by key and 
# ascending/descending order by value

d = {'Oil': 230, 'Clip': 150, 'Stud': 175}

print('Original dictionary:', d)

d1 = sorted(d.items())
print('Ascending order by key:', d1)

d2 = sorted(d.items(), reverse = True)
print('Descending order by key:', d2)

d3 = sorted(d.items(), key = lambda x: x[1])
print('Ascending order by values:', d3)

d4 = sorted(d.items(), key = lambda x: x[1], reverse = True)
print('Descending order by values:', d4)
