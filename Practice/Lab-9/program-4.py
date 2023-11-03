# A list contains names of boys and girls as its elements. Boy's names are stored as tuple.
# Write a program to find out number of boys and girls in the list

l = ['Rick', 'Subinay', 'Munmun', 'Shubham', 'Payel', 'Nibedita', 'Partha', 'Moumita', 'Koyel']

boys = ['Rick', 'Subinay', 'Shubham', 'Partha']

n_girls = 0
for i in l:
    if i not in boys:
        n_girls += 1

print('No. of boys:', len(boys))
print('No. of girls:', n_girls)
