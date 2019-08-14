# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Emily Murphy
# 	 		Ryan Oakes
# 	 		Kelsey Wright
#			Mason Fields
# Section:		102-522
# Assignment:	Lab 7
# Date:		10/7/2018

done = False  # for the while loop to keep process going
productionLevels = []  # list of the production levels
# loop for user to input widgets
while not done:
    widgets = int(input("Enter the number of widgets created or enter a negative number to stop: "))  # ask users for widgets
    if widgets < 0:  # stops the loop if user enters negative number
        done = True
    else:
        productionLevels.append(widgets)  # adds the production level/widgets to a list

# For loop to find if the the percentages of increasing and decreasing
for intervalSize in range(1, len(productionLevels)):
    increasing = 0  # increasing starts at 0
    decreasing = 0  # decreasing starts at 0
    total = 0  # total to find the percentages
    # for loop to check each interval
    for i in range(0, len(productionLevels) - intervalSize):
        total += 1  # total of #day intervals
        if productionLevels[i + intervalSize] - productionLevels[i] > 0:  # if the interval is increasing
            increasing += 1  # add 1 to increasing for each interval that is increasing
        if productionLevels[i + intervalSize] - productionLevels[i] < 0:  # if the interval is decreasing
            decreasing += 1  # add 1 to decreasing for each interval that is increasing
    print("For", intervalSize, end="")
    print("-day intervals", round((increasing / total * 100), 1), end="")
    print("% were increasing and", round((decreasing / total * 100), 1), end="")
    print("% were decreasing")

