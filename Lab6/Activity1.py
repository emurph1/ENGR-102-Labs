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
# Test Case 1: (x+2)(x-1)(x-4) = x^3 - 3x^2 - 6x + 8 --> 3 roots and check is b >= a + 1 (a = 2 and b = 6)
# Test Case 2: (x+1)(x-2)^2 = x^3 - 5x^2 + 8x - 4 --> 2 roots and check is b >= a + 1 (a = 1 and b = 3)
# Test Case 3: (x+1)^3 = x^3 + 3x^2 - 3x + 1 --> 1 root and check is b >= a + 1 (a = -2 and b = 0)
# Test Case 4:  x^3 + 2x^2 + 3x + 4  --> 1 roots and check is b >= a + 1 (a = -2 and b = 0)

coefficientA = float(input('Enter coefficient A: '))  # user inputs coefficient A
coefficientB = float(input('Enter coefficient B: '))  # user inputs coefficient B
coefficientC = float(input('Enter coefficient C: '))  # user inputs coefficient C
coefficientD = float(input('Enter coefficient D: '))  # user inputs coefficient D
a = float(input('Enter value for a: '))  # user inputs a value
b = float(input('Enter value for b: '))  # user inputs b value
fA = coefficientA * math.pow(a, 3) + coefficientB * math.pow(a, 2) + coefficientC * a + coefficientD  # evaluating f(A)
fB = coefficientA * math.pow(b, 3) + coefficientB * math.pow(b, 2) + coefficientC * b + coefficientD  # evaluating f(B)
p = (a + b) / 2  # finding the midpoint
fP = coefficientA * math.pow(p, 3) + coefficientB * math.pow(p, 2) + coefficientC * p + coefficientD
iterations = 0  # starting number of iterations
found = False
while not found:  # keep loop going while p is not the real root
    iterations += 1
    p = (a + b) / 2  # midpoint (a,b)
    fP = coefficientA * math.pow(p, 3) + coefficientB * math.pow(p, 2) + coefficientC * p + coefficientD
    if fP == 0:  # function evaluated at p = 0
        found = True
        iterations += 1
    elif fP > 0:  # function evaluated at p is greater than 0
        if fA > fB:  # checks for fA being the upper bound
            a = p  # resetting upper bound
            fA = coefficientA * math.pow(a, 3) + coefficientB * math.pow(a, 2) + coefficientC * a + coefficientD  # reevaluating a
        else:  # fB is the upper bound
            b = p  # resetting upper bound
            fA = coefficientA * math.pow(b, 3) + coefficientB * math.pow(b, 2) + coefficientC * b + coefficientD  # reevaluating b
        iterations += 1
    else:  # function evaluated at p is less than 0
        if fA < fB:  # checking for fA being the lower bound
            a = p  # resetting upper bound
            fA = coefficientA * math.pow(a, 3) + coefficientB * math.pow(a, 2) + coefficientC * a + coefficientD  # reevaluating a
        else:  # checking for fB being the lower bound
            b = p  # resetting lower bound
            fA = coefficientA * math.pow(b, 3) + coefficientB * math.pow(b, 2) + coefficientC * b + coefficientD  # reevaluating b
print('The root is ', p)
print('It took', iterations, 'iterations to find the root')