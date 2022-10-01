def findPermutation(p, q):
    r = []
    for item in q:
        r.append(p.index(item)+1)

    return r
