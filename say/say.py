nulls = [
        'zero', 'ten', 'hundred', 'thousand', 'million', 'billion', 'trillion'
    ]

def prehandred_name(index):    
    tens = [
        '', nulls[1], 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen'] + [i + 'teen' for i in units[4:]]
    nums = [nulls[0]] + units[1:] + [nulls[1]] + teens[1:]    
    for i in range(2, 10):
        nums += [tens[i]] + [tens[i] + '-' + unit for unit in units[1:]]

    return nums[index]

def temp():
    return [10**i for i in range(12, 2, -3)] + [100, 10, 0]


def get_name(number):
    components = []
    if number > 99:
        for base in temp()[:-2]:
            hundreds = int(number / base)
            assert(hundreds < 100)
            lowest = hundreds % 100
            hundreds = int(hundreds / 100)
            assert(lowest < 100)
            if lowest + hundreds > 0:
                if hundreds > 0:
                    components += [prehandred_name(hundreds)]
                if lowest > 0:                    
                    components.append(prehandred_name(lowest))
                bases = temp()
                components.append(nulls[-bases.index(base) - 1])
                number = number - (hundreds * 100 + lowest) * base    

    if number != 0:
        components.append(prehandred_name(number))

    return ' '.join(components)


def say(number):
    if number < 0 or number > 999999999999:
        raise AttributeError('Value does not fit in range')

    if number == 0:
        return 'zero'
    
    return get_name(number)
