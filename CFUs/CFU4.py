# By submitting this assignment, I agree to the following:
# #  “Aggies do not lie, cheat, or steal, or tolerate those who do”
# #  “I have not given or received any unauthorized aid on this assignment”
# # Emily Murphy
# # ENGR 102-552
# # CFU 4
# # 10/10/2018

num = int(input('Enter number to find factorial (not 0): '))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print('The factorial of', num, 'is', factorial)



