# coding=utf-8
# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”

# Emily Murphy
# Mason Fields
# Kelsey Wright
# Ryan Oakes
# Lab 02 Activity 3 - using linear interpolation to find the position of a car along a racetrack
# 09/05/2018

import math

distCar1 = 50  # first measurement of car
distCar2 = 615  # second car measurement
time1 = 30  # first measurement of time
time2 = 45  # second measurement of time
slope = (distCar2 - distCar1) / (time2 - time1) # slope of car to be used in linear interpolation
calcTime = 37  # given time to be used to find car position after 37 seconds
calcTime2 = 1200  # 20 minutes converted to seconds
timePass = calcTime - time1  # to correctly find carPosition, need time passed from time1 to calcTime
timePass2 = calcTime2 - time1  # to correctly find carPosition, need time passed from time1 to calcTime
radius = 500  # given radius of race track in METERS
circumference = 2 * math.pi * radius  # circumference of racetrack
carPosition1 = ((slope * timePass) + distCar1) % circumference  # carPosition after 37 sec
carPosition2 = ((slope * timePass2) + distCar1) % circumference  # carPosition after 20 min

print("Starting time:", time1)
print("Seconds after the starting time:", calcTime)
print("Seconds after the starting time:", calcTime2)
print("The car will be", carPosition1, "meters after", calcTime, "seconds")
print("The car will be", carPosition2, "meters after", calcTime2, "seconds or 20 minutes")
