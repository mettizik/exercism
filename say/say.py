nulls = [
        '', 'ten', 'hundred', 'thousand', 'million', 'billion', 'trillion'
    ]

def prehandred_name(index):    
    tens = [
        '', nulls[1], 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen'] + [i + 'teen' for i in units[4:]]
    nums = [''] + units[1:] + [nulls[1]] + teens[1:]    
    for i in range(2, 10):
        nums += [tens[i]] + [tens[i] + '-' + unit for unit in units[1:]]

    return nums[index]

bases = [0, 10, 100] + [10**i for i in range(3, 13, 3)]

def add_basename(components, base):
    if base >= 100:
        components.append(nulls[bases.index(base)])

def get_base_text(hundreds, rest, base, components):    
    if rest + hundreds > 0:        
        if hundreds > 0:
            components += [prehandred_name(hundreds)]
            add_basename(components, 100)
            if rest > 0:
                components.append('and')

        if rest > 0:
            components.append(prehandred_name(rest))

        add_basename(components, base)
        return True

    return False

def split_number_to_parts(number, base):
    stripped = int(number / base)
    hundreds = int(stripped / 100)
    assert(hundreds < 10)
    lowest = stripped % 100
    assert(lowest < 100)
    return hundreds, lowest

def get_name(number):
    components = []
    bases = [0, 10, 100] + [10**i for i in range(3, 13, 3)]
    if number > 99:
        for base in bases[-1:1:-1]:
            hundreds, lowest = split_number_to_parts(number, base)
            if get_base_text(hundreds, lowest, base, components):
                number = number - (hundreds * 100 + lowest) * base

        if number != 0:
            components.append('and')

    if number != 0:
        get_base_text(0, number, 0, components)

    return ' '.join(components)


def say(number):
    if number < 0 or number > 999999999999:
        raise AttributeError('Value does not fit in range')

    if number == 0:
        return 'zero'
    
    return get_name(number)

say(1234)
