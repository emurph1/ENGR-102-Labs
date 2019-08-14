# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Emily Murphy
#               Kelsey Wright
#               Ryan Oakes
#               Mason Fields
# Section:		102-522
# Assignment:	Lab10
# Date:		5/11/2018

# “As a team, we
# have gone through all required sections of the tutorial, and each team member
# understands the material.

import numpy as np
A = np.random.random((3, 4))  # 3x4 matrix
B = np.random.random((4, 2))  # 4x2 matrix
C = np.random.random((2, 3))  # 2x3 matrix
D = np.random.random((3, 1))  # 3x1 matrix
E = A @ B @ C  # A * B * C is E matrix
print('Matrix E is:', E)
print('Transposed E is:', E.T)
x = np.linalg.solve(E, D)  # solving for x from the linear system Ex = D
print('X value from Ex = D is: ', x)