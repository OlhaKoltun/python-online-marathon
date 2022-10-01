def order(source):
    RESULT = ('ascending', 'descending', 'not sorted')
    result_index = None
    if source[1] > source[0]:
        result_index = 0
    elif source[1] < source[0]:
        result_index = 1
    else:
        result_index = 2

    for i in range(2, len(source)):
        if source[i] > source[i-1] and result_index == 0:
            continue
        elif source[i] < source[i-1] and result_index == 1:
            continue
        else:
            result_index = 2
            break

    return RESULT[result_index]
