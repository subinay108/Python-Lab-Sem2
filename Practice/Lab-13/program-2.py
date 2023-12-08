# Write a program that proves that if the dictionary returned by locals() is manipulated, the values
# of original variables don't change
variable = 10

def function():
    localDict = locals()
    localDict['variable'] = 20

print('Before function call: ', variable)
function()
print('After function call: ', variable)