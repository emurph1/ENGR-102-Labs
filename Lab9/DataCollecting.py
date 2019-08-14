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


# COLLECT DATA PART
fileName = input('Enter file name (without extension): ') + '.dat'  # user enters file name
independent = input('Enter name of independent variable: ')  # user inputs independent variable name
dependent = input('Enter name of dependent variable: ')   # user inputs dependent variable name
entries = int(input('Enter amount of data entries for dependent and independent: '))  # user enters # of data entries
listI = []  # list of independent variable values
listD = []  # list of dependent variable values

# list to add values for independent values list
for i in range(entries):
    x = int(input('Enter values for ' + independent + ': '))  # user enters values for independent variable
    listI.append(x)
# list to add values for dependent values list
for j in range(entries):
    y = int(input('Enter values for ' + dependent + ': '))  # user enters values for dependent variable
    listD.append(y)

# open file and add the independent and dependent variable values
with open(fileName, 'w') as f:
    print(independent + "\'s: ")
    # look at each item in list of independent variable values
    for item in listI:
        f.write(str(item))
    print(dependent + "\'s: ")
    # look at each num in list of dependent variable values
    for num in listD:
        f.write(str(num))


