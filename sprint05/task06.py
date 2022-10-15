# Write  the function check_positive(number) whose input parameter is a number. 

class MyError(Exception):
    def __init__(self, _data):
        self.data = _data

    def __str__(self):
        return self.data

def check_positive(num):
    try:
        num = float(num)
        if num < 0:
            raise MyError(f'You input negative number: {num}. Try again.')
        return f'You input positive number: {num}'
    except MyError as e:
        return e
    except ValueError:
        return 'Error type: ValueError!'
