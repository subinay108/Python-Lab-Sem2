# While purchasing certail items, a discount of 10% if offered if the quantity
# purchased is more than 1000. If quantity and price per item are input through keyboard,
# Write a program to calculate the total expenses
quantity = int(input('Enter quantity: '))
price = float(input('Enter price per item: '))

expenses = quantity * price

if expenses > 1000:
    expenses = expenses * 0.9

print('Total Expenses:', expenses)