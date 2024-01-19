# WAP to perform radixSort
from random import shuffle

def radixSort(a):
    numDict = {}
    for i in range(10):
        numDict[i] = []
    
    # get the no. of digits of highest number
    maxDigits = len(str(max(a)))

    divisor = 10 ** maxDigits
    while divisor > 0:
        
        divisor //= 10
    

arr = list(range(1, 11))
shuffle(arr)
print('Before Sorting:', arr)

radixSort(arr)
print('After Sorting:', arr)