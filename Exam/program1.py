# Date: 19-01-2024
# 5. a) Write a python program to calculate the area of a circle using the math module

from math import pi

radius = float(input('Enter the radius: '))

area = pi * (radius ** 2)

print('Area of circle:', area)