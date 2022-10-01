def Cipher_Zeroes(N):
    points = 0
    for character in N:
        if character in ('0', '6', '9'):
            points += 1
        elif character == '8':
            points += 2

    if points > 0:
        if points % 2 == 0:
            points -= 1
        else:
            points += 1

    str_point = str(bin(points))
    str_point = str_point[str_point.index('b')+1:]

    return int(str_point[str_point.index('b')+1:])
