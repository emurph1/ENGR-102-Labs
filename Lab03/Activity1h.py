# coding=utf-8
# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”

# Emily Murphy
# Mason Fields
# Kelsey Wright
# Ryan Oakes
# Lab 03 Activity 1h
# ENGR 102-522
# 09/12/2018
import math

magnitude1 = float(input("Enter Richter Scale value: "))  # Richter Scale value 1
magnitude2 = float(input("Enter Richter Scale value: "))  # Richter Scale value 2
difference = 32 ** math.fabs(magnitude1 - magnitude2)
print("Two Richter scale values of", magnitude1, "and", magnitude2, "have a energy release ration of", difference, "Joules")