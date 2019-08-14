# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Emily Murphy
# ENGR 102-552
# CFU 1
# 10/01/2018
import math

# Code to find the area of a circle
radius = 3.21
area = math.pi * (radius ** 2)
print('Area is ', area)

# Code to find the circumference of a circle
circumference = 2 * math.pi * radius
print('Circumference is', circumference)

# Calculating the side length of square from area of circle
sideLength = math.sqrt(area / math.pi) # finding side length with height and squareArea
print('Side length of square from area of circle is', sideLength)

# Calculating the side length from the circumference of the circle
sideLengthC = (circumference / 2) / math.pi  # calculation to find side length from square circumference
print('Side length of square from circumference is', sideLengthC)