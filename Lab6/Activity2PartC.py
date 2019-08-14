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
# Date:		10/7/2018
import math
x = int(input('Enter x value: '))
a = 0.1
function1 = math.sin(5 * x)  # original function1 = sin(5x)
function2 = 2 * (math.sin(x ** 2))  # original function2 = 2sin(x^2)
function3 = 4 * math.cos(x) + 2 * math.sin(x)  # original function3 = 4cos + 2sinx
function4 = math.e ** (2 * x)  # original function4 = e^(2x)
function1A = math.sin(5 * (x + a))  # f(x+a) of function1
function2A = 2 * (math.sin((x + a) ** 2))  # f(x+a) of function2
function3A = 4 * math.cos((x + a)) + 2 * math.sin((x + a))  # f(x+a) of function3
function4A = math.e ** (2 * (x + a))  # f(x+a) of function4
derivF1 = (function1A - function1) / a  # (f(x+a) - f(x)) / a for function 1
derivF2 = (function2A - function2) / a  # (f(x+a) - f(x)) / a for function 2
derivF3 = (function3A - function3) / a  # (f(x+a) - f(x)) / a for function 3
derivF4 = (function4A - function4) / a  # (f(x+a) - f(x)) / a for function 4
derivN1 = 0  # this to use in loop to evaluate successive values against the derivF1
derivN2 = 0  # this to use in loop to evaluate successive values against the derivF2
derivN3 = 0  # this to use in loop to evaluate successive values against the derivF3
derivN4 = 0  # this to use in loop to evaluate successive values against the derivF4
iterations1 = 0  # defining iterations for function1 to later be calculated in loop
iterations2 = 0  # defining iterations for function2 to later be calculated in loop
iterations3 = 0  # defining iterations for function3 to later be calculated in loop
iterations4 = 0  # defining iterations for function4 to later be calculated in loop
found = False  # implemented in the loop to keep running it until derivative of each function is found
found2 = False
found3 = False
found4 = False
# while loop to find the derivatives of function1
while not found:
    iterations1 += 1
    if derivN1 == 0 or (derivN1 - abs(derivF1)) > (1 * (10 ** -6)):
        derivN1 = derivF1  # way of storing past derivative to evaluate with new
        a /= 2
        function1A = math.sin(5 * (x + a))  # redefining f(x+a) of function1
        derivF1 = (function1A - function1) / a  # redefining (f(x+a) - f(x)) / a for function 1
    elif (derivN1 - abs(derivF1)) < (1 * (10 ** -6)):
        found = True

# for function2
while not found2:
    iterations2 += 1
    if derivN2 == 0 or (derivN2 - abs(derivF2)) > (1 * (10 ** -6)):
        derivN2 = derivF2  # way of storing past derivative to evaluate with new
        a /= 2
        function2A = 2 * (math.sin((x + a) ** 2))  # redefining f(x+a) of function2
        derivF2 = (function2A - function2) / a  # redefining (f(x+a) - f(x)) / a for function 1
    elif (derivN2 - abs(derivF2)) < (1 * (10 ** -6)):
        found2 = True

# for function3
while not found3:
    iterations3 += 1
    if derivN3 == 0 or (derivN3 - abs(derivF3)) > (1 * (10 ** -6)):
        derivN3 = derivF3  # way of storing past derivative to evaluate with new
        a /= 2
        function3A = 4 * math.cos((x + a)) + 2 * math.sin((x + a))  # redefining f(x+a) of function3
        derivF3 = (function3A - function3) / a  # redefining (f(x+a) - f(x)) / a for function 1
    elif (derivN3 - abs(derivF3)) < (1 * (10 ** -6)):
        found3 = True

# for function4
while not found4:
    iterations4 += 1
    if derivN4 == 0 or (derivN4 - abs(derivF4)) > (1 * (10 ** -6)):
        derivN4 = derivF4  # way of storing past derivative to evaluate with new
        a /= 2
        function4A = math.e ** (2 * (x + a))  # redefining f(x+a) of function4
        derivF4 = (function3A - function3) / a  # redefining (f(x+a) - f(x)) / a for function 1
    elif (derivN4 - abs(derivF4)) < (1 * (10 ** -6)):
        found4 = True

print('From the function sin(5x), the computed derivative at x =', x, 'is', derivN1)
print('Finding the derivative of function1 took ', iterations1, 'iterations')
print('From the function 2(sin(x^2)), the computed derivative at x =', x, 'is', derivN2)
print('Finding the derivative of function1 took ', iterations2, 'iterations')
print('From the function 4cos(x) + 2sin(x), the computed derivative at x =', x, 'is', derivN3)
print('Finding the derivative of function1 took ', iterations3, 'iterations')
print('From the function e^(2x), the computed derivative at x =', x, 'is', derivN4)
print('Finding the derivative of function1 took ', iterations4, 'iterations')