# If basic salary is less than Rs. 1500, then HRA = 10% of basic salary and DA = 90% of basic salary.
# If salary is either equal to or above Rs.1500, then HRA = Rs.500 and DA = 98% of basic salary.
# If the employee's salary is input through the keyboard, write a program to find his gross salary.
salary = int(input('Enter Salary: '))

if salary < 1500:
    HRA = salary * 0.1
    DA = salary * 0.9
else:
    HRA = 500
    DA = salary * 0.98

grossSalary = salary + HRA + DA

print("Employee's gross salary: ", grossSalary)