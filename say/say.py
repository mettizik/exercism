nulls = [
        'zero', 'ten', 'hundred', 'thousand', 'million', 'billion', 'trillion'
    ]

def prehandred_name(index):    
    tens = [
        '', nulls[1], 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen'] + [i + 'teen' for i in units[4:]]
    nums = [nulls[0]] + units[1:] + [nulls[1]] + teens[1:]    
    for i in range(2, 10):
        nums += [tens[i]] + [tens[i] + '-' + unit for unit in units[1:]]

    return nums[index]

def get_name(number):
    components = []
    bases = [0, 10, 100] + [10**i for i in range(3, 13, 3)]
    if number > 99:
        for base in bases[-1:1:-1]:
            stripped = int(number / base)
            lowest = stripped % 100
            assert(lowest < 100)
            hundreds = int(stripped / 100)
            assert(hundreds < 10)            
            if lowest + hundreds > 0:
                number = number - (hundreds * 100 + lowest) * base
                if hundreds > 0:
                    components += [prehandred_name(hundreds)]
                    components.append(nulls[bases.index(100)])
                    if lowest > 0:
                        components.append('and')

                if lowest > 0:
                    components.append(prehandred_name(lowest))
                    
                components.append(nulls[bases.index(base)])

        if number != 0:
            components.append('and')

    if number != 0:
        components.append(prehandred_name(number))

    return ' '.join(components)


def say(number):
    if number < 0 or number > 999999999999:
        raise AttributeError('Value does not fit in range')

    if number == 0:
        return 'zero'
    
    return get_name(number)

say(810000)