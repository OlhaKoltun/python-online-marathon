def studying_hours(a):
    length = 1
    max_len = 1

    for i in range(len(a) - 1):
        if a[i] <= a[i + 1]:
            length += 1
        else:
            if length > max_len:
                max_len = length
            length = 1

    if length > max_len:
        max_len = length

    return max_len
