# Write  the function divide(numerator, denominator) the two input parameters of which are numbers. 
# The function returns the result of dividing two numbers.

def divide(numerator, denominator):
    try:
        result = numerator / denominator
        return f'Result is {result}'
    except ZeroDivisionError:
        return f'Oops, {numerator}/0, division by zero is error!!!'
    except TypeError:
        return 'Value Error! You did not enter a number!'
