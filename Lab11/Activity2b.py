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
# Date:		14/11/2018

import numpy as np

x = []
y = []
qValue = float(input('Enter query value: '))
fileN = input('Enter file name along with extension: ')  # user enters file name

# open the file to add data to lists
with open(fileN, 'r') as f:
    for line in f:
        x.append(float(line.split()[0]))  # add x values to x list
        y.append(float(line.split()[1]))  # add y values to y list


def inter(xV, yV, num):
    upperI = 0
    lowerI = 0
    for i in range(len(xV)):
        if num < xV[i] < lowerI:  # finding the index of the lowest x value
            lowerI = i
        if upperI < xV[i] < num:  # finding the index of the greatest x value
            upperI = i
    slope = (yV[upperI] - yV[lowerI]) / (xV[upperI] - xV[lowerI])  # slope from the interpolation equation
    equation = slope * (num - xV[lowerI]) + yV[lowerI]  # the full linear equation
    return equation


print(inter(x, y, qValue))
dim = int(input('Enter number of dimensions: '))  # dimensions for the array given multiple dimensions for inter
npArray = np.array([])
with open(fileN, "r") as f:
    iteration = 0
    for line in f:
        for i in range(dim):
            value = np.array([float(line.split()[i])])
            npArray = np.append(npArray, value)
        iteration += 1
    npArray = npArray.reshape(iteration, dim)

print('Value at query value is: ', npArray)
