# As input data, you have a list of strings.
# Write a method double_string() for counting the number of strings
# from the list, represented in the form of the concatenation of two
# strings from this arguments  list

def double_string(data):
    counter = 0
    for part1 in data:
        if any(part1 + part2 in data for part2 in data):
            counter += 1

    return counter
