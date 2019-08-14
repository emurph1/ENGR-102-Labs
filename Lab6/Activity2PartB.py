# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Emily Murphy
# 	 		Ryan Oakes
# 	 		Kelsey Wright
#			Mason Fields
# Section:		102-522
# Assignment:	Lab 6
# Date:		10/3/2018

import math
# Finding the derivative numerically
# Test polynomial: x^3 - 3x^2 - 6x + 8

coefficientA = int(input('Enter coefficient A: '))  # user inputs coefficient A
coefficientB = int(input('Enter coefficient B: '))  # user inputs coefficient B
coefficientC = int(input('Enter coefficient C: '))  # user inputs coefficient C
coefficientD = int(input('Enter coefficient D: '))  # user inputs coefficient D
x = float(input('Enter x to be evaluated in derivative of function: '))  # user inputs x value
derivativeA = coefficientA * 3  # finding the derivative of Ax^3
derivativeB = coefficientB * 2  # finding derivative of Bx^2
derivativeC = coefficientC * 1  # finding the derivative or Cx
dOfF = derivativeA * (x ** 2) + derivativeB * x + derivativeC  # f'(x) and then plugging in x value --> Part A
a = 0.1  # set a value
fX = coefficientA * math.pow(x, 3) + coefficientB * math.pow(x, 2) + coefficientC * x + coefficientD  # function f(x)
fXA = coefficientA * math.pow((x + a), 3) + coefficientB * math.pow((x + a), 2) + \
      coefficientC * (x + a) + coefficientD  # function f(x + a)
derivative = (fXA - fX) / a  # f(x+a) - f(x) / a
derivativeN = 0
iterations = 0  # setting iterations to 1 if the
found = False  # for the loop to continue till found derivative
# loop to find the derivative numerically
while not found:  # loop runs until derivative is found
    iterations += 1  # counter
    # assigning derivativeN in order to find the difference of successive values in loop
    if derivativeN == 0 or (derivativeN - derivative) > (1 * 10 ** -6):
        derivativeN = derivative  # assigning derivative to derivativeN
        a /= 2  # redefining a
        fXA = coefficientA * math.pow((x + a), 3) + coefficientB * math.pow((x + a), 2) + \
            coefficientC * (x + a) + coefficientD  # function f(x + a) --> redefining with new a value
        derivative = (fXA - fX) / a  # f(x+a) - f(x) / a --> new derivative value to be run with derivativeN
    elif (derivativeN - derivative) < (1 * 10 ** -6):  # if derivative is less than 0.000006, loop stops
        found = True

print('(f(x +a) - f(x)) / a) at x = ', x, 'is', derivativeN)
print('The difference between the analytical and numerical derivative is', dOfF - derivative)
print('It took', iterations, 'iterations')
