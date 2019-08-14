# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Emily Murphy
# Section:		102-522
# Assignment:	CFU 6
# Date:		31/10/2018
tempsList1 = []  # list for temps from first week
tempsList2 = []  # list for temps from second week
temps = open('Temperature.dat', 'r')  # open the temp data file
# loops to add data in file to list
for item in temps.read()[:7]:  # first week
    tempsList1.append(int(item))
for item in temps.read()[8:13]:  # second week
    tempsList2.append(int(item))
temps.close()  # closing file
with open('WeeklyAverages.dat', 'w') as data:  # open file to write the weekly averages
    # loops to find averages and printing the averages
    for num in tempsList1:
        total = 0  # sum starts at 0
        total += num  # sum of the numbers
        print('Average for first week is: ', data.write(str(total/7)))
    for num in tempsList2:
        total = 0  # sum starts at 0
        total += num  # sum of the numbers
        print('Average for second week is: ', data.write(str(total/7)))
print(tempsList1)
print(tempsList2)