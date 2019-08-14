a = 2
b = 0
try:
    c = a / b
except ZeroDivisionError:
    print('You cannot divide by zero!')
    b = int(input('Enter new number: '))
    c = a / b
print(c)