def filterBible(scripture, book, chapter):
    destination = []

    for item in scripture:
        if item[:2] == book and item[2:5] == chapter:
            destination.append(item)

    return destination
