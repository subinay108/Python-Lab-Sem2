# Date: 19-01-2024
# 5. b) Write a python program that takes n integers from the user and creates a dictionary whose 
# keys are the integers and whose values are "even" or "odd" depending on the number. 
# e.g. if the entered numbers are 12 23 35, the program creates the dictionary 
# {12: 'Even', 23: 'Odd', 35: 'Odd'}

# Function to check Odd or Even
def checkOddEven(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# Input numbers and save it in a list
numberList = map(int, input('Enter numbers: ').split())

# Create empty dictionary
numberDict = {}

# Insert numbers in dictonary 
for i in numberList:
    numberDict[i] = checkOddEven(i)

# Print result dictonary
print(numberDict)