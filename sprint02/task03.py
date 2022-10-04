def calculate_distance(point1, point2):

    return math.sqrt((point2[0] - point1[0])**2
                     + (point2[1] - point1[1])**2)


def figure_perimetr(test):
    pattern = '[LBRT]{2}\d:\d'
    result = re.findall(pattern, test)
    points = {}
    for item in result:
        point = (int(item[2]), int(item[4]))
        points[item[:2]] = point

    perimetr = 0
    perimetr += calculate_distance(points['LB'], points['RB']) \
                + calculate_distance(points['LB'], points['LT']) \
                + calculate_distance(points['RT'], points['LT']) \
                + calculate_distance(points['RT'], points['RB'])

    return round(perimetr, 14)
