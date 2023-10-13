# Write a program to receive radius of circle and length and breadth of a rectangle in one call to
# input. Calculate and print the circumference of circle and perimeter of rectangle.
from math import pi
r = float(input('Enter the radius: '))
print('Cicumference:', 2 * pi * r)

l = float(input('Enter length: '))
b = float(input('Enter breadth: '))
print('Perimeter:', l * b)