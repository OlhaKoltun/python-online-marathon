# Create function create_account(user_name: string, password: string, secret_words: list). This function should return inner function check.
# The function check compares the values of its arguments with password and secret_words: 
# the password must match completely, secret_words may be misspelled (just one element).
# Password should contain at least 6 symbols including one uppercase letter, one lowercase letter,  special character and one number.
# Otherwise function create_account raises ValueError. 

import re

def compare_secret_words(lst1, lst2):
    is_equal = False
    if len(lst1) == len(lst2):
        diff = [item for item in lst1 if item not in lst2]
        if len(diff) <= 1:
            is_equal = True

    return is_equal

def create_account(user_name, password, secret_words):
    
    def check(inner_password, inner_secret_words):
        if password == inner_password\
                and compare_secret_words(secret_words, inner_secret_words):
            return True
        else:
            return False

    password_pattern = '(?=.*[0-9])(?=.*[!@#$%^&*_])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*_]{6,}'
    
    if re.match(password_pattern, password):
        return check
    else:
        raise ValueError
