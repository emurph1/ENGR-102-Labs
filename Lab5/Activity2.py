# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Emily Murphy
# 	 		Ryan Oakes
# 	 		Kelsey Wright
#			Mason Fields
# Section:		102-522
# Assignment:	Lab 5
# Date:		9/26/2018

gender = input('Enter gender as Male or Female: ')
age = int(input('Enter age: '))
cholesterol = int(input('Enter cholesterol level: '))
smokerOrNo = input('Enter Yes or No if you are a smoker: ')
HDL = int(input('Enter HDL number (in mg/dl): '))
systolicBP = int(input('Enter systolic BP (in mmHg): '))
treatOrNoTreat = input('Enter Yes or No if your systolic BP has been treated: ')  # connection to systolic BP → changes amount of points
pointTotal = 0  # from the beginning, start out with 0 points then added with other factors like age
risk = 0

# THIS WHOLE SECTION IS BASED OFF FEMALE POINT SYSTEM
#  Assigning points according to age input
if gender == 'Female':
    if 20 <= age <= 34:
        pointTotal = -7
    elif 35 <= age <= 39:
        pointTotal = -3
    elif 40 <= age <= 44:
        pointTotal = 0
    elif 45 <= age <= 49:
        pointTotal = 3
    elif 50 <= age <= 54:
        pointTotal = 6
    elif 55 <= age <= 59:
        pointTotal = 8
    elif 60 <= age <= 64:
        pointTotal = 10
    elif 65 <= age <= 69:
        pointTotal = 12
    elif 70 <= age <= 74:
        pointTotal = 14
    elif 75 <= age <= 79:
        pointTotal = 16
    else:
        print('We do not have data for your age')

    #  Adding points to pointTotal according to cholesterol and age
    if cholesterol < 160:
        pointTotal += 0
    elif 160 <= cholesterol <= 199 and 20 <= age <= 39:
        pointTotal += 4
    elif 160 <= cholesterol <= 199 and 40 <= age <= 49:
        pointTotal += 3
    elif 160 <= cholesterol <= 199 and 50 <= age <= 59:
        pointTotal += 2
    elif 160 <= cholesterol <= 199 and 60 <= age <= 69:
        pointTotal += 1
    elif 200 <= cholesterol <= 239 and 20 <= age <= 39:
        pointTotal += 8
    elif 200 <= cholesterol <= 239 and 40 <= age <= 49:
        pointTotal += 6
    elif 200 <= cholesterol <= 239 and 50 <= age <= 59:
        pointTotal += 4
    elif 200 <= cholesterol <= 239 and 60 <= age <= 69:
        pointTotal += 2
    elif 200 <= cholesterol <= 239 and 70 <= age <= 79:
        pointTotal += 1
    elif 240 <= cholesterol <= 279 and 20 <= age <= 39:
        pointTotal += 11
    elif 240 <= cholesterol <= 279 and 40 <= age <= 49:
        pointTotal += 8
    elif 240 <= cholesterol <= 279 and 50 <= age <= 59:
        pointTotal += 5
    elif 240 <= cholesterol <= 279 and 60 <= age <= 69:
        pointTotal += 3
    elif 240 <= cholesterol <= 279 and 70 <= age <= 79:
        pointTotal += 2
    elif cholesterol >= 280 and 20 <= age <= 39:
        pointTotal += 13
    elif cholesterol >= 280 and 40 <= age <= 49:
        pointTotal += 10
    elif cholesterol >= 280 and 50 <= age <= 59:
        pointTotal += 7
    elif cholesterol >= 280 and 60 <= age <= 69:
        pointTotal += 4
    else:
        pointTotal += 2

    #  Adds points to pointTotal according to smoker and nonsmoker and age
    if smokerOrNo == 'No':
        pointTotal += 0
    elif smokerOrNo == 'Yes' and 20 <= age <= 39:
        pointTotal += 9
    elif smokerOrNo == 'Yes' and 40 <= age <= 49:
        pointTotal += 7
    elif smokerOrNo == 'Yes' and 50 <= age <= 59:
        pointTotal += 4
    elif smokerOrNo == 'Yes' and 60 <= age <= 69:
        pointTotal += 2
    elif smokerOrNo == 'Yes' and 70 <= age <= 79:
        pointTotal += 1

    # Add points to pointTotal based on HDL
    if HDL >= 60:
        pointTotal += -1
    elif 50 <= HDL <= 59:
        pointTotal += 0
    elif 40 <= HDL <= 49:
        pointTotal += 1
    elif HDL < 40:
        pointTotal += 2
    if pointTotal < 9:
        risk = str("<1%")

    #  Adds points to pointTotal according to systolic BP
    if systolicBP < 120:
        pointTotal += 0
    elif 120 <= systolicBP <= 129 and treatOrNoTreat == 'No':
        pointTotal += 1
    elif 120 <= systolicBP <= 129 and treatOrNoTreat == 'Yes':
        pointTotal += 3
    elif 130 <= systolicBP <= 139 and treatOrNoTreat == 'No':
        pointTotal += 2
    elif 130 <= systolicBP <= 139 and treatOrNoTreat == 'Yes':
        pointTotal += 4
    elif 140 <= systolicBP <= 159 and treatOrNoTreat == 'No':
        pointTotal += 3
    elif 140 <= systolicBP <= 159 and treatOrNoTreat == 'Yes':
        pointTotal += 5
    elif systolicBP >= 160 and treatOrNoTreat == 'No':
        pointTotal += 4
    elif systolicBP >= 160 and treatOrNoTreat == 'Yes':
        pointTotal += 6

    # finding risk based off of pointTotal
    if pointTotal < 9:
        risk = str('<1% risk')
    elif pointTotal == 9 and pointTotal == 10 and pointTotal == 11 and pointTotal == 12:
        risk = str('1% risk')
    elif pointTotal == 13 and pointTotal == 14:
        risk = str('2% risk')
    elif pointTotal == 15:
        risk = str('3% risk')
    elif pointTotal == 16:
        risk = str('4% risk')
    elif pointTotal == 17:
        risk = str('5% risk')
    elif pointTotal == 18:
        risk = str('6% risk')
    elif pointTotal == 19:
        risk = str('8% risk')
    elif pointTotal == 20:
        risk = str('11% risk')
    elif pointTotal == 21:
        risk = str('14% risk')
    elif pointTotal == 22:
        risk = str('17% risk')
    elif pointTotal == 23:
        risk = str('22% risk')
    elif pointTotal == 24:
        risk = str('27% risk')
    elif pointTotal >= 25:
        risk = str('30% or higher')

# BASED OFF MALE POINT SYSTEM
# assigns points based off of age
if gender == "Male":
    # assigns points based off of age
    if age <= 34:
        pointTotal -= 9
    elif 34 < age <= 39:
        pointTotal -= 4
    elif 39 < age <= 44:
        pointTotal += 0
    elif 44 < age <= 49:
        pointTotal += 3
    elif 49 < age <= 54:
        pointTotal += 6
    elif 54 < age <= 59:
        pointTotal += 8
    elif 59 < age <= 64:
        pointTotal += 10
    elif 64 < age <= 69:
        pointTotal += 11
    elif 69 < age <= 74:
        pointTotal += 12
    else:
        pointTotal += 13

    # assigns points based off of cholesterol and age
    if cholesterol < 160:
        pointTotal += 0
    elif cholesterol < 200:
        if age < 40:
            pointTotal += 4
        elif age < 50:
            pointTotal += 3
        elif age < 60:
            pointTotal += 2
        elif age < 70:
            pointTotal += 1
        else:
            pointTotal += 0
    elif cholesterol < 240:
        if age < 40:
            pointTotal += 7
        elif age < 50:
            pointTotal += 5
        elif age < 60:
            pointTotal += 3
        elif age < 70:
            pointTotal += 1
        else:
            pointTotal += 0
    elif cholesterol < 280:
        if age < 40:
            pointTotal += 9
        elif age < 50:
            pointTotal += 6
        elif age < 60:
            pointTotal += 4
        elif age < 70:
            pointTotal += 2
        else:
            pointTotal += 1
    else:
        if age < 40:
            pointTotal += 11
        elif age < 50:
            pointTotal += 8
        elif age < 60:
            pointTotal += 5
        elif age < 70:
            pointTotal += 3
        else:
            pointTotal += 1

    # assigns points based off of smoking habits and age
    if smokerOrNo == "Yes":
        pointTotal += 0
    else:
        if age < 40:
            pointTotal += 8
        elif age < 50:
            pointTotal += 5
        elif age < 60:
            pointTotal += 3
        elif age < 70:
            pointTotal += 1
        else:
            pointTotal += 1

    # assigns points based off of HDL
    if HDL >= 60:
        pointTotal -= 1
    elif HDL >= 50:
        pointTotal += 0
    elif HDL >= 40:
        pointTotal += 1
    else:
        pointTotal += 2

    # assigns points based on systolic BP as well as if it has been treated or not
    if systolicBP < 120:
        if treatOrNoTreat == "No":
            pointTotal += 0
        else:
            pointTotal += 0
    elif systolicBP < 130:
        if treatOrNoTreat == "No":
            pointTotal += 0
        else:
            pointTotal += 1
    elif systolicBP < 140:
        if treatOrNoTreat == "No":
            pointTotal += 1
        else:
            pointTotal += 2
    elif systolicBP < 160:
        if treatOrNoTreat == "No":
            pointTotal += 1
        else:
            pointTotal += 2
    else:
        if treatOrNoTreat == "No":
            pointTotal += 2
        else:
            pointTotal += 3

    # assigns risk based off of point total
    if pointTotal < 0:
        risk = "<%1"
    elif pointTotal < 5:
        risk = "1%"
    elif pointTotal < 7:
        risk = "2%"
    elif pointTotal == 7:
        risk = "3%"
    elif pointTotal == 8:
        risk = "4%"
    elif pointTotal == 9:
        risk = "5%"
    elif pointTotal == 10:
        risk = "6%"
    elif pointTotal == 11:
        risk = "8%"
    elif pointTotal == 12:
        risk = "10%"
    elif pointTotal == 13:
        risk = "12%"
    elif pointTotal == 14:
        risk = "16%"
    elif pointTotal == 15:
        risk = "20%"
    elif pointTotal == 16:
        risk = "25%"
    else:
        risk = ">= 30%"

print('Your 10-year risk is', risk)