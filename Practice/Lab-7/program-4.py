#  A company insures its drivers in the following cases-
# - If the driver is married
# - If the driver is unmarried, male & above 30 years of age
# - If the driver is unmarried, female & above 25 years of age
# If the marital status, sex and age of the dirver are the inputs, Write a program to determine
# whetether the driver should be insured or not
mStatus = input('Enter marital status(married/ unmarried): ')
sex = input('Enter sex(male/ female): ')
age = int(input('Enter age: '))

isInsured = False

if mStatus == 'married':
    isInsured = True
else:
    if sex == 'male' and age > 30:
        isInsured = True
    elif sex == 'female' and age > 25:
        isInsured = True

if isInsured:
    print('Driver should be insured')
else:
    print("Driver shouldn't be insured")