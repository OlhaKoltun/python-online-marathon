# Write  the function check_number_group(number) whose input parameter is a number. 

class ToSmallNumberGroupError(Exception):
    def __init__(self, _data):
        self.data = _data

    def __str__(self):
        return self.data

def check_number_group(num):
    try:
        num = int(num)
        if num <= 10:
            raise ToSmallNumberGroupError("We obtain error:Number of your group can't be less than 10")
        return f'Number of your group {num} is valid'
    except ToSmallNumberGroupError as e:
        return e
    except ValueError:
        return 'You entered incorrect data. Please try again.'
