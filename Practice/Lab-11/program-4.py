# WAP that defines a function ispalindrome() which checks whether a given string is a palindrome or
# not. Ignore spaces and case mismatch while checking for palindrome

string = input('Enter a string: ')

def ispalindrome(string):
    string = string.replace(' ', '') # removes spaces
    string = string.upper() # convert the string to uppercase
    
    flag = True
    for i in range(len(string)//2): # checks upto middle of the string
        if string[i] != string[-(i + 1)]: # if the element from both ends are equal or not
            flag = False
            break
    
    return flag

print('Given string is palindrome: ', ispalindrome(string))
