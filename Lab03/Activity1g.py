# coding=utf-8
# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”

# Emily Murphy
# Mason Fields
# Kelsey Wright
# Ryan Oakes
# Lab 03 Activity 1g
# ENGR 102-522
# 09/12/2018

import math

voltage = float(input("Enter voltage: "))  # user inputs voltage
dB = 20 * math.log(voltage, 10)  # conversion of voltage to dB
print(voltage, "volts is ", dB, "decibels")
