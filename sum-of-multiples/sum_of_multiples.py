def sum_of_multiples(limit: int, bases: list):
    multiples = []
    for i in bases:
        multiples += [ numb for numb in range(limit) if numb % i == 0 ]

    return sum(set(multiples))
