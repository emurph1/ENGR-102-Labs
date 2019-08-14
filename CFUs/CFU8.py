# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Emily Murphy
# Section:		102-522
# Assignment:	CFU 8
# Date:		12/11/2018

import webbrowser

url1 = input('Enter url 1: ')  # user inputs url 1
url2 = input('Enter url 2: ')  # user inputs url 2

webbrowser.open_new(url1)
webbrowser.open_new_tab(url2)
#Tested with https://www.google.com