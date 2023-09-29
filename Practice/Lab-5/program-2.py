# WAP to find the min difference between all the pair of elements in an array

arr = [5, 3, 9, 1, 2]

arr.sort() # n(log n)

minDif = max(arr) - min(arr)

for i in range(len(arr) - 1):
    if minDif > abs(arr[i + 1] - arr[i]):
        minDif = abs(arr[i + 1] - arr[i])

for i in range(len(arr) - 1):
    if minDif == abs(arr[i + 1] - arr[i]):
        print(arr[i + 1], ', ', arr[i])

