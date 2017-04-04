def distance(lhs, rhs):
    if len(lhs) != len(rhs):
        raise ValueError('Comparands length does not match')

    dist = 0
    for i in range(len(lhs)):
        if lhs[i] != rhs[i]:
            dist += 1

    return dist
