# Write  the function day_of_week(day) whose input parameter is a number or string representation of number. 

class RangeError(Exception):
    def __init__(self, _data):
        self.data = _data

    def __str__(self):
        return self.data

def day_of_week(day):
    week = {1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'}
    try:
        day = int(day)
        if day < 1 or day > 7:
            raise RangeError('There is no such day of the week! Please try again.')
        return week[day]
    except RangeError as r:
        return r
    except ValueError:
        return 'You did not enter a number! Please try again.'
