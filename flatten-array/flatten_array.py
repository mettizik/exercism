def filter_nulls(func):
    def wrapper(inputs):
        return func(list(filter(lambda a: not a is None, inputs)))
    return wrapper

@filter_nulls
def flatten(inputs):
    retvals = []
    for i in inputs:
        if isinstance(i, list):
            retvals += flatten(i)
        else:
            retvals.append(i)

    return sorted(list(set(retvals)))
