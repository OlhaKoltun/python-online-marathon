# Using regular expression write method max_population()
# for parsing strings and get info about location with highest population

def max_population(data):
    max_p = 0
    country = ''
    for i in range(1, len(data)):
        p = re.search(r'[0-9]{5}', data[i])
        if int(p.string[p.start():p.end()]) > max_p:
            max_p = int(p.string[p.start():p.end()])
            country = re.search(r'[a-z]{2}_[a-z]+', data[i])

    return country.string[country.start():country.end()], max_p
