# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Emily Murphy
#               Kelsey Wright
#               Ryan Oakes
#               Mason Fields
# Section:		102-522
# Assignment:	Lab11
# Date:		12/11/2018

tol = 1e-6
# function F
def F(x):
    return x ** 3 - x ** 2 + x + 1

# derivative of function F
def deriv(X , dX = 0):
    if dX == 0:
        dX = tol * X
    return (F(X + dX) - F(X)) / dX

# newton_step function
def newton_step(x):
    estimate = 0
    if estimate == 0:
        estimate = tol * guess
    else:
        estimate = estimate
    value = x - F(x) / deriv(x, estimate)
    return value

# newton function to find sequence of values until no more than 10^-6
def newton(guess, estimate=0):
    approx = []
    iterations = 0
    if estimate == 0:
        estimate = tol * guess
    else:
        estimate = estimate
    nextG = newton_step(guess)  # for next time thru the loop
    root = nextG - F(nextG) / deriv(nextG, estimate)
    while not (- tol < root - nextG < tol):  # keep finding root till diff no more than 1e-6
        nextG = root
        root = nextG - F(nextG) / deriv(nextG, estimate)
        approx.append(root)
        iterations += 1
    print('It took', iterations, 'iterations')
    return approx

guess = float(input('Enter guess: '))
print('Root list: ', newton(guess))