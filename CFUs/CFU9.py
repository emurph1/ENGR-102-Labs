# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Emily Murphy
# Section:		102-522
# Assignment:	CFU 09
# Date:		19/11/2018
from math import cos
from math import sin

# function to find the cartesian coordinates
def cartesian(rV, theta):
    x = rV * cos(theta)  # finding the x value
    y = rV * sin(theta)  # finding the y value
    cartesianC = x, y  # putting the coordinates in point form
    return cartesianC  # return the point

r = int(input('Enter r value: '))  # user enters the r value
theta = float(input('Enter degree value: '))  # user enters theta in degrees
# print out the cartesian coordinates
print('Cartesian coordinates are: ', cartesian(r, theta))
