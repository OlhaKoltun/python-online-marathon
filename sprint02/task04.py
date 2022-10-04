# As input data, you have a string that consists of words that
# have duplicated characters at the end of it.
# All duplications may be in the next format:
# - wordxxxx
# - wordxyxyxy
# - wordxyzxyzxyz
# where x, xy or xyz repeated ending of the word
#
# Using re module write function pretty_message() that remove all duplications

def pretty_message(data):
    return re.sub(r'([a-z]+?)\1+', r'\1', data)
