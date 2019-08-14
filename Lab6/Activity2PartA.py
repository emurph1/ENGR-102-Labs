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


# Finding the derivative analytically
# Test polynomial: x^3 - 3x^2 - 6x + 8
coefficientA = int(input('Enter coefficient A: '))  # user inputs coefficient A
coefficientB = int(input('Enter coefficient B: '))  # user inputs coefficient B
coefficientC = int(input('Enter coefficient C: '))  # user inputs coefficient C
coefficientD = int(input('Enter coefficient D: '))  # user inputs coefficient D
x = float(input('Enter x to be evaluated in derivative of function: '))  # user inputs x value
derivativeA = coefficientA * 3  # finding the derivative of Ax^3
derivativeB = coefficientB * 2  # finding derivative of Bx^2
derivativeC = coefficientC * 1  # finding the derivative or Cx
# No derivative of D since D is a constant
dOfF = derivativeA * (x ** 2) + derivativeB * x + derivativeC  # f'(x) and then plugging in x value
print('The derivative is', derivativeA, 'x^2 +', derivativeB, 'x +', derivativeC)
print('f\'(x) at x =', x, 'is', dOfF)
