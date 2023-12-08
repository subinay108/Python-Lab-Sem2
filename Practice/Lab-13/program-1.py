# Date: 08/12/2023
# Write a program that proves that the dictionary returned by globals() can be used to manipulate
# values of variables in it
variable = 10

def function():
    globalDict = globals()
    globalDict['variable'] = 20

print('Before function call: ', variable)
function()
print('After function call: ', variable)
