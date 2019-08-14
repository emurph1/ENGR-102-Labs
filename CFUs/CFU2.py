# By submitting this assignment, I agree to the following:
# #  “Aggies do not lie, cheat, or steal, or tolerate those who do”
# #  “I have not given or received any unauthorized aid on this assignment”
# # Emily Murphy
# # ENGR 102-552
# # CFU 2
# # 10/01/2018

name = input('Enter name: ')  # user inputs name
total = 0  # defines total of scores to then be used in average calculation
avg = 0  # defines average then to be redefined in the for loop
# loop so user can input three test scores
for i in range(3):
    score = int(input('Enter score for tests: '))  # user inputs 3 test scores
    total += score  # redefining total
    avg = total / 3  # finding average of test scores from total and number of inputs
print(name, ' Your average score on tests is a', avg)