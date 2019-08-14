# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Emily Murphy
#               Kelsey Wright
#               Ryan Oakes
#               Mason Fields
# Section:		102-522
# Assignment:	Lab10
# Date:		27/11/2018

from math import *

Epsilon = 1E-6

class RiemannResult:
   """
   Contains the results of a Riemann sum operation.
   """
   def __init__(self):
       self.iterations = 0
       self.lastArea = 0
       self.area = 0
       self.complete = False

    def getInput():
       print("This program will evaluate the definite integral of a formula using various kinds of Riemann sum.")
       lowerBound = float(input("Enter lower bound: "))
       upperBound = float(input("Enter upper bound: "))
       formulaOk = False
       while not formulaOk:
           formula = input("Enter formula to integrate, using x as the variable: ")
           if "^" not in formula: # Look for ^, which is the bitwise XOR operator to Python and the exponent operator to people
               formulaOk = True
           else:
               # Make sure the user didn't mean to use ** instead of ^
               print("You used '^' in your formula. This likely means you want a power, but it will actually be interpreted as bitwise XOR.")
               print("To raise a number to a power, use the ** operator or the pow function.")
               formulaOk = input("Is your formula ({}) correct? ".format(formula)).lower() in ['y', 'yes']
       return formula, lowerBound, upperBound

    def integral(formula, lowerBound, upperBound):
       divisions = 10
       leftRes = RiemannResult()
       rightRes = RiemannResult()
       midpointRes = RiemannResult()
       trapezoidRes = RiemannResult()
       formulaFunc = eval("lambda x: " + formula) # i love letting people execute arbitrary code
       print("Calculating, please wait (this might take a WHILE!)")
       while not (trapezoidRes.complete and leftRes.complete and rightRes.complete and midpointRes.complete): # while any sum is incomplete
           dx = (upperBound - lowerBound) / divisions
           # For each sum, if it's incomplete, move the last area to lastArea, scrub the area variable, and increase iterations
           if not leftRes.complete:
               leftRes.iterations += 1
               leftRes.lastArea = leftRes.area
               leftRes.area = 0
           if not rightRes.complete:
               rightRes.iterations += 1
               rightRes.lastArea = rightRes.area
               rightRes.area = 0
           if not midpointRes.complete:
               midpointRes.iterations += 1
               midpointRes.lastArea = midpointRes.area
               midpointRes.area = 0
           if not trapezoidRes.complete:
               trapezoidRes.iterations += 1
               trapezoidRes.lastArea = trapezoidRes.area
               trapezoidRes.area = 0
           # Now calculate each Riemann sum (at once)
           for i in range(0, divisions):
               # Left endpoint rectangles
               if not leftRes.complete:
                   h = formulaFunc(lowerBound + dx * i)
                   leftRes.area += h * dx
               # Right endpoint rectangles
               if not rightRes.complete:
                   h = formulaFunc(lowerBound + dx * (i + 1))
                   rightRes.area += h * dx
               # Midpoint rectangles
               if not midpointRes.complete:
                   h = formulaFunc(lowerBound + dx * (i + 0.5))
                   midpointRes.area += h * dx
               # Trapezoids
               if not trapezoidRes.complete:
                   # Trapezoid area = 1/2 * b * (h_1 + h_2)
                   h1 = formulaFunc(lowerBound + dx * i)
                   h2 = formulaFunc(lowerBound + dx * (i + 1))
                   trapezoidRes.area += 0.5 * dx * (h1 + h2)
           if abs(leftRes.area - leftRes.lastArea) < Epsilon:
               if not leftRes.complete: print("Left Riemann sum has converged.") # only print this once
               leftRes.complete = True
           if abs(rightRes.area - rightRes.lastArea) < Epsilon:
               if not rightRes.complete: print("Right Riemann sum has converged.")
               rightRes.complete = True
           if abs(midpointRes.area - midpointRes.lastArea) < Epsilon:
               if not midpointRes.complete: print("Midpoint Riemann sum has converged.")
               midpointRes.complete = True
           if abs(trapezoidRes.area - trapezoidRes.lastArea) < Epsilon:
               if not trapezoidRes.complete: print("Trapezoid Riemann sum has converged.")
               trapezoidRes.complete = True
           divisions += 1 # Increase divisions for the next go around, if there is one...
           if divisions % 2000 == 0:
               print("Still going...") # Let the user know we haven't deadlocked
       return leftRes, rightRes, midpointRes, trapezoidRes

    def printResults(formula, lowerBound, upperBound, leftRes, rightRes, midpointRes, trapezoidRes):

       print("The integral of {} from {} to {} according to various methods is...".format(formula, lowerBound, upperBound))
       print("LEFT RIEMANN SUM: {:.6f} ({} iterations)".format(leftRes.area, leftRes.iterations))
       print("RIGHT RIEMANN SUM: {:.6f} ({} iterations)".format(rightRes.area, rightRes.iterations))
       print("MIDPOINT RIEMANN SUM: {:.6f} ({} iterations)".format(midpointRes.area, midpointRes.iterations))
       print("TRAPEZOID RIEMANN SUM: {:.6f} ({} iterations)".format(trapezoidRes.area, trapezoidRes.iterations))

    formula, lowerBound, upperBound = getInput() # Get our formula, lower bound, upper bound
    leftRes, rightRes, midpointRes, trapezoidRes = integral(formula, lowerBound, upperBound) # Get our Riemann sums
    printResults(formula, lowerBound, upperBound, leftRes, rightRes, midpointRes, trapezoidRes)
