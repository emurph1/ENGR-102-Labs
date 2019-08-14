# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Emily Murphy
# 	 		Ryan Oakes
# 	 		Kelsey Wright
#			Mason Fields
# Section:		102-522
# Assignment:	Lab 4
# Date:		19/9/2018

a = bool(int(input('Enter a integer: ')))
b = bool(int(input('Enter a integer: ')))
c = bool(int(input('Enter a integer: ')))

# PART A
print(a and b and c)  # output 1
print(a or b or c)  # output 2
print((not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b))  # output 3
print((not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b
and c) or (a and ((b and not c) or (not b)))))  # output 4

# Part B
print(((not a) and b) or (a and (not b)))  # output 5
print((a and b and c) or (a and (not b) and (not c)) or ((not a) and b and (not c)) or ((not a) and (not b) and c)  # output 6
# Part C
print((not a) and (not c) or (not b))) # output 7
print(a or c and (not b))  # output 8