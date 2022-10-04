# Numbers in the Morse code have the following pattern:
#
# - all digits consist of 5 characters;
# - the number of dots at the beginning indicates the numbers from 1 to 5,
# the remaining characters are dashes;
# - starting with the number 6, each dot is replaced by a dash and vise versa.
# Write the function morse_number() for encryption of a number
# in a three-digit format in Morse code.
#
# Attention!
# Do not use any collection data like lists, tuples,
# dictionaries for holding Morse codes

def morse_number(string):
    result = ''
    for item in string:
        if item == '0':
            result += '----- '
        elif item == '1':
            result += '.---- '
        elif item == '2':
            result += '..--- '
        elif item == '3':
            result += '...-- '
        elif item == '4':
            result += '....- '
        elif item == '5':
            result += '..... '
        elif item == '6':
            result += '-.... '
        elif item == '7':
            result += '--... '
        elif item == '8':
            result += '---.. '
        elif item == '9':
            result += '----. '

    return result.rstrip()
