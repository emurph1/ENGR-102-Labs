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
# Date:		27/11/2018

import numpy as np
import matplotlib.pyplot as plt

degrees = int(input("How many degrees is the polynomial? >>> "))
domain_boundary = 10
domain = np.array(range(-domain_boundary, domain_boundary + 1))


def build_coefficients(num_of_degrees):
    coefficients = []
    for i in (range(num_of_degrees + 1)):
        current_degree = num_of_degrees - i
        if i != degrees:
            coefficients.append(float(input("What is the coefficient for the term x^" + str(current_degree) + "? >>> ")))
        else:
            coefficients.append(float(input("What is the coefficient for the last term? >>> ")))
    return coefficients


def find_derivative(num_of_degrees, coefficients):
    new_coefficients = []
    for i in range(num_of_degrees):
        new_coefficients.append((num_of_degrees - i) * coefficients[i])
    return new_coefficients


def evaluate(num_of_degrees, coefficients, x_values):
    values = []
    for x in x_values:
        temp_value = 0
        for i in range(num_of_degrees + 1):
            temp_value += coefficients[i] * pow(x, num_of_degrees - i)
        values.append(temp_value)
    return values


def extrema_finder(x_values, y_values):
    extrema = []

    for i in range(len(x_values) - 2):
        if i != 0 or i != (len(x_values) - 2):
            if y_values[i] > y_values[i - 1] and y_values[i] > y_values[i + 1]:
                extrema.append([x_values[i], y_values[i]])
            elif y_values[i] < y_values[i - 1] and y_values[i] < y_values[i + 1]:
                extrema.append([x_values[i], y_values[i]])

    return extrema


# Function calculations
coeff = build_coefficients(degrees)  # Building initial coefficients
function_y_values = evaluate(degrees, coeff, domain)  # Finding y values of function
function_extrema = extrema_finder(domain, function_y_values)  # Finding extrema values of function

# Derivative calculations
first_derivative = find_derivative(degrees, coeff)  # Finding first derivative
first_derivative_y_values = evaluate(degrees - 1, first_derivative, domain)  # Finding y values of first derivative
first_derivative_extrema = extrema_finder(domain, first_derivative_y_values) # Finding extrema values of derivative

degrees = degrees - 1  # Setting it down a power

# Second derivative calculations
second_derivative = find_derivative(degrees, first_derivative)  # Finding second derivative
second_derivative_y_values = evaluate(degrees - 1, second_derivative, domain)  # Finding y values of second derivative
second_derivative_extrema = extrema_finder(domain, second_derivative_y_values)  # Finding extrema values of second derivative

print(function_y_values)
print(first_derivative_y_values)
print(second_derivative_y_values)

fig, ax1 = plt.subplots()
plt.xlabel("X Values")
plt.ylabel("Y values")
plt.title("Graph of the Function, First Derivative, and Second Derivative")

color = 'black'
ax1.plot(domain, function_y_values, color=color)

for point in function_extrema:
    ax1.plot(point[0], point[1], 'ro', color=color)

color = 'blue'
ax1.plot(domain, first_derivative_y_values, color=color)

for point in first_derivative_extrema:
    ax1.plot(point[0], point[1], 'ro', color=color)

color = 'red'
ax1.plot(domain, second_derivative_y_values, color=color)

for point in second_derivative_extrema:
    ax1.plot(point[0], point[1], 'ro', color=color)

plt.show()
