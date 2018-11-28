from math import *
function = input("Enter a function f(x):\n")
for row in range(10, -11, -1):
    for column in range(-10, 11):
        function_output  = function.replace('x', str(column), function.count('x'))        
        if eval(function_output) == row:
            print('o', end='')
        elif row  == 0 and column == 0:
            print('+', end='')
        elif column == 0:
            print('|', end='')
        elif row == 0:
            print('-', end='')
        else:
            print(' ', end = '')
        function_output = function
    print()