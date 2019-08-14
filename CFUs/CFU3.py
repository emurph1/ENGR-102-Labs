# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Emily Murphy
# ENGR 102-552
# CFU 3
# 10/03/2018

homework = int(input('Enter homework grade: '))  # user inputs homework grade
exam = int(input('Enter exam grade: '))  # user inputs exam score
outside = input('Enter Yes if you did an outside project and No if you didn\'t: ')  # user inputs outside project
numGrade = 0  # starting numGrade
numGrade += exam * 0.6  # adding homework score to overall with the weight of exam (60%)
numGrade += homework * 0.4  # adding homework score to overall with the weight of homework (40%)
# conditional to add 5 extra points with outside project
if outside == 'Yes':
    numGrade += 5
# Conditionals that find letter grade and print the letter grade
if numGrade >= 90 and outside == 'Yes':
    print('You get an A')
elif numGrade >= 90 and outside == 'No':
    print('You would\'ve gotten an A, but did not do the outside project. You get a B.')
elif 80 <= numGrade < 90:
    print('You get an B')
elif 70 <= numGrade < 80:
    print('You get an C')
elif 60 <= numGrade < 70:
    print('You get an D')
else:
    print('You get an F')