# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Emily Murphy
# 	 		Ryan Oakes
# 	 		Kelsey Wright
#			Mason Fields
# Section:		102-522
# Assignment:	Lab 8
# Date:		10/22/2018

# Get all the inputs - RYAN
x1 = int(input("Enter x value of first pair of data: ")) # user enters the first x coordinate
y1 = int(input("Enter y value of first pair of data: ")) # user enters the first y coordinate
x2 = int(input("Enter x value of second pair of data: ")) # user enters the second x coordinate
y2 = int(input("Enter y value of second pair of data: ")) # user enters the second y coordinate
x = int(input("Enter x value that you want to find the value of y for: "))

# Find the slope from data pairs - EMILY
# This is to find the slope which is then applied in the linear interpolation/extrapolation equation
slope = (y2 - y1) / (x2 - x1)

# Solve the equation with the inputted x value - MASON
equation = (slope * (x - x1)) + y2  # This is the linear interpolation equation

#print the y value - KELSEY
print('Y-value is', equation)
