def flatten(inputs):
    retvals = []
    for i in list(filter(lambda a: not a is None, inputs)):
        if isinstance(i, list):
            retvals += flatten(i)
        elif not (isinstance(i, tuple) and not i):
            retvals.append(i)

    return retvals
