# Write a program that prints all unique combinations of 1, 2 and 3

s = '123456'
arr = []
def permute(a):
    # base condition
    if len(a) == len(s):
        arr.append(a)
        return
    
    # recurrence condition
    for i in s: 
        if i not in a:
            permute(a + i) 

permute('')

print(len(arr))

# for i in arr:
#     print(i) 