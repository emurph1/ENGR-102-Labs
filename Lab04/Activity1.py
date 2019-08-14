# coding=utf-8
# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
#  Names: 	Emily Murphy
#  	 		Ryan Oakes
# 	 		Kelsey Wright
# 			Mason Fields
# Section:		102-522
# Assignment:	Lab 4
# Date:		19/9/2018
import math

tolerance = 0.0001

# Example 1
x = (1/3) * (1/3)  # multiplying fractions
y = 0.3333 * 0.3333  # multiplying decimal of fraction
print(x)
print(y)
print('Is x the same as y')
print(x == y)
print('Is x within tolerance of y')
if abs(x - y) < tolerance:
    print('Values are the same')
else:
    print('Values not the same')

# Example 2 --> whole number times fraction
x = 18 * (1/3)
y = 18 * 0.33333
print(x)
print(y)
print('Is x the same as y')
print(x == y)
print('Is x within tolerance of y')
if abs(x - y) < tolerance:
    print('Values are the same')
else:
    print('Values not the same')

# Example 3 --> fractions
a = 1/12
print(a)
b = a * 12
print(b)
c = 10 * a
d = 2 * a
e = c + d
print(e)
print('Is b the same as e')
print(b == e)
print('Is b within tolerance of e')
if abs(b - e) < tolerance:
    print('Values are the same')
else:
    print('Values not the same')

# Example 4 --> math square root
from math import *
x = sqrt(1/6)
print(x)
y = x **2 * 6
print(y)
z = x * 6 * x
print(z)
print('Is y the same as z')
print(y == z)
print('Is y within tolerance of z')
if abs(y - z) < tolerance:
    print('Values are the same')
else:
    print('Values not the same')

# Example 5 --> addition of percents
a = 4.567
b = 85.654
c = 9.779
sum1 = a + b + c
print(sum1)
a = 5
b = 86
c = 10
sum2 = a + b + c
print(sum2)
print('Are the sums the same?')
print(sum1 == sum2)
print('Is sum1 within tolerance of sum2')
if abs(sum1 - sum2) < tolerance:
    print('Values are the same')
else:
    print('Values not the same')

# Example 6 --> scientific notation + sig fig
a = 1.26894 * (10 ** 4)
b = 1.269 * (10 ** 4)  # if you were restricted by sig figs, values would be different
print(a)
print(b)
print('Is a the same as b')
print(a == b)
print('Is a within tolerance of b')
if abs(a - b) < tolerance:
    print('Values are the same')
else:
    print('Values not the same')

# Example 7 --> using pi
x = (9 * math.pi) ** 10
y = (9 * 3.14159265359) ** 10
print(x)
print(y)
print('Is x the same as y')
print(x == y)
print('Difference is', y - x)
print('Is x within tolerance of y')
if abs(x - y) < tolerance:
    print('Values are the same')
else:
    print('Values not the same')

# Example 8 --> using natural log
x = e ** 2
y = 2.71828 ** 2
print(x)
print(y)
print('Is x the same as y')
print(x == y)
print('Is x within tolerance of y')
if abs(x - y) < tolerance:
    print('Values are the same')
else:
    print('Values not the same')

# Part 3
print('THIS IS PART 3')
tolerance = 0.00001
a = e ** 2
b = 2.71828 ** 2
print(a)
print(b)
if abs(a - b) < tolerance:
    print('Values are the same')
else:
    print('Values not the same')
x = (1/3) * (1/3)  # multiplying fractions
y = 0.3333 * 0.3333  # multiplying decimal of fraction
print(x)
print(y)
if abs(x - y) < tolerance:
    print('Values are the same')
else:
    print('Values not the same')
