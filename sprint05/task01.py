# Write the function valid_email(...) to check if the input string is a valid email address or not.

import re


class InvalidEmail(Exception):
    def __init__(self, _data):
        self.data = _data

    def __str__(self):
        return repr(self.data)


def valid_email(email):
    try:
        pattern = '[a-z0-9._%+-]+@[a-z.-]+\.[a-z]{2,}'
        if not re.match(pattern, email):
            raise InvalidEmail('Email is not valid')

    except InvalidEmail as e:
        return e.data

    return 'Email is valid'
