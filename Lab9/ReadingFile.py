# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Emily Murphy
#               Kelsey Wright
#               Ryan Oakes
#               Mason Fields
# Section:		102-522
# Assignment:	Lab9
# Date:		29/10/2018

# ASSUMING THERE ARE 2 PAIRS OF DATA IN DATA FILE IN THE ORDER: x1, x2, y1, y2
fileName = input('Enter file name (without extension): ') + '.dat'  # user input file name
listNums = []  # list of numbers in data file
# loop so user can enter interpolate values and adds those values to list
with open(fileName, 'r') as f:
    # loop to add each item in the data file to list of numbers
    for item in f.read():
        listNums.append(int(item))
slope = ((listNums[3] - listNums[2]) / (listNums[1] - listNums[0]))  # slope in interpolation formula
done = False
while not done:
    x = int(input('Enter values to interpolate and enter negative number to stop: '))  # user enters values to interpolate
    if x < 0:
        done = True
    else:
        equation = (slope * (x - listNums[0])) + listNums[3]
        print('At x =', x, 'y value is', equation)