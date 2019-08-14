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

import matplotlib.pyplot as plt
import numpy as np

# First Graph
t = np.arange(0, 5, 0.01)
s = np.exp(t)
plt.plot(t, s)
plt.xlabel('Years')
plt.ylabel('Number of Cells in Body (in millions)')
plt.title('Representation of Number of Cells in the Body over 10 Years')
plt.grid(True)
plt.show()
# Second Graph --> API
t1 = np.arange(0, 4.0, 0.2)
t2 = np.arange(0, 4.0, 0.04)
plt.title('Graph of Sound Wave')
plt.plot(t2, np.cos(2 * np.pi * t2))
plt.ylabel('Amplitude (in micrometers)')
plt.xlabel('Wavelength (in micrometers)')
plt.show()

# RYAN'S CODE
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
              27, 28, 29, 30])
plt.plot(x*2.35)
plt.ylabel("Price you pay ($)")
plt.xlabel("Amount of Gas Pumped (Gallons)")
plt.title("Price You Pay ($) vs Amount of Gas Pumped (Gallons)")
plt.show()
# GPA of students
x = np.arange(5)
GPA = [4.0, 2.0, 3.3, 2.6, 3.8]
plt.bar(x, GPA)
plt.xticks(x, ("Bill", "Trey", "Suzy", "Haley", "Bobby"))
plt.ylabel("GPA")
plt.title("GPA of Students")
plt.show()

# KELSEY'S CODE
x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
plt.plot(x*2.35)
plt.ylabel("Price you pay ($)")
plt.xlabel("Amount of Gas Pumped (Gallons)")
plt.title("Price You Pay ($) vs Amount of Gas Pumped (Gallons)")
plt.show()

# GPA of students
x = np.arange(5)
GPA= [4.0, 2.0, 3.3, 2.6, 3.8]

plt.bar(x,GPA)
plt.xticks(x,("Bill", "Trey", "Suzy", "Haley", "Bobby"))
plt.ylabel("GPA")
plt.title("GPA of Students")
plt.show()


# MASON'S CODE
t = np.arange(0., 10., 1)  # creating values
plt.plot(t, t*10, 'bo', t, t*10, 'k',)  # plot type
plt.title("Acceleration of an airplane")  # title of graph
plt.xlabel('Time (s)')  # label of x axis
plt.ylabel('velocity (mph)')  # label of y axis
plt.grid(True)  # turn on grid
plt.show()  # display graph

data = {'a': np.arange(60), 'd': np.random.randn(60)}  # data
data['b'] = data['a'] + 10 * np.random.randn(60)  # random value
data['d'] = np.abs(data['d']) * 100  # random value
plt.grid(True)  # turn on grid
plt.scatter('a', 'b', c='c', s='d', data=data)  # scatter plot
plt.xlabel('GPD (Hundreds of billions)')  # label of x axis
plt.ylabel('Life Expectancy (years)')  # label of the y axis
plt.show()  # display graph