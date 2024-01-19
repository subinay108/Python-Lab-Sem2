# WAP to perform radixSort
from random import shuffle

def radixSort(a):
    numDict = {}
    for i in range(10):
        numDict[i] = []
    

arr = list(range(1, 11))
shuffle(arr)
print('Before Sorting:', arr)

radixSort(arr)
print('After Sorting:', arr)