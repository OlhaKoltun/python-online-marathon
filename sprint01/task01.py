def kthTerm(n, k):
    result = 0
    for i in range(6, -1, -1):
        if k >= 2 ** i:
            result += n ** i
            k -= 2 ** i

    return result
