# Percentage marks obtained by a student are input through the keyboard. The student gts a division
# as per following rules:-
# Percentage above or equal to 60 -> 1st Division
# Percentage between 50 and 59 -> 2nd Division
# Percentage between 40 and 49 -> 3rd Division
# Percentage less than 40 -> Fail

marks = float(input('Enter you marks: '))

if marks >= 60:
    print('1st Division')
elif marks >= 50:
    print('2nd Division')
elif marks >= 40:
    print('3rd Division')
else:
    print('Fail')

