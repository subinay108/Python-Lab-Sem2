# Date: 03/11/2023
# Create a list of 5 names - 'Anil', 'Amol', 'Aditya', 'Avi', 'Alka'
# Insert a name 'Anuj' before 'Aditya'
# Append a name 'Zulu'
# Delete 'Avi' from the list
# Replace 'Anil' with 'Anil Kumar'

l = ['Anil', 'Amol', 'Aditya', 'Avi', 'Alka']

pos = l.index('Aditya')
l.insert(pos, 'Anuj')

l.append('Zulu')

l.remove('Avi')

pos = l.index('Anil')
l[pos] = 'Anil Kumar'

print(l)