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
# Date:		10/10/2018

scoreSum = []  # list of score sums of each golfer
infoSum = {}  # dictionary that has name and sum of scores
scores = []  # list of scores
while True:  # loop to save info of golfers and scores
    firstScore = int(input('Enter first round score: '))  # user inputs first score
    if firstScore > 0:  # to exclude 'stop' from lists
        secondScore = int(input('Enter second round score: '))  # user inputs second score
        name = input('Enter golfer name: ')  # user input golfer name
        scores.append(firstScore)  # add scores to scores list
        scores.append(secondScore)  # add scores to scores list
        scoreSum.append(firstScore + secondScore)  # adds total scores to a list
        infoSum[name] = firstScore + secondScore
    elif firstScore < 0:  # stop loops when use inputs a neg number for first score
        break

# loop to sort the scores list
swapped = True
while swapped:
    for k in range(len(scores) - 1, 0, -1):  # to look at all numbers in list
        swapped = False
        for i in range(k, 0, -1):  # looking at each number from right to left
            if scores[i] < scores[i - 1]:  # checking if scores is less than the number before
                scores[i], scores[i - 1] = scores[i - 1], scores[i]  # swaps numbers if true
                swapped = True

        for i in range(k):  # looking at each number from left to right
            if scores[i] > scores[i + 1]:  # checking if scores is greater than the the next
                scores[i], scores[i + 1] = scores[i + 1], scores[i]  # swaps numbers if true
                swapped = True

# Finding the median value
half = len(scores) // 2  # finding the index number of median
median = 0
if not half % 2:  # checking if there is a remainder in half
    median = scores[half]
else:  # finds the median if half has a remainder
    left = scores[half - 1]  # finds the number that is left of the scores[half] value
    right = scores[half]  # finds the number that is right of the scores[half] value
    median = (left + right) / 2

# Finding the winners
for i in scoreSum:
    if i < median:  # score has to be less than median
        for names in infoSum:  # loop to find where i is in infoSum dictionary
            if infoSum[names] == i:  # once found where i is, print the names associated
                print(names)
