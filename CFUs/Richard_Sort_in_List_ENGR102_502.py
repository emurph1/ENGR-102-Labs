# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Emily Murphy
# Richard_Sort_in_List_ENGR102_502.py
# CFU 5
# 10/17/2018

heightList = []  # heights list
heightInCenti = 0  # variable to be changed in while loop to make all heights in centimeters before adding to list
# loop for user to enter in heights in feet and inches to then be converted to cm then to be added to list
while True:
    height = input('Enter height in feet then inches:')  # user inputs height
    feet = int(height[0]) * 12  # converting first str in height list into integer and then feet to inches
    total = feet + int(height[2])  # adding the total together
    heightList.append(total * 2.54)  # first convert to cm then add to list
    if height == '0 0':  # stops the loop if user enters '0 0'
        heightList.pop(-1)  # removes the last value, which would be 0 0
        break

# loop to print out all the heights (in cm) in order of input
for num in heightList:
    print('Height in cm is:', num)

