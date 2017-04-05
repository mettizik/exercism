def prehandred_name(index):
    nulls = [
        'zero', 'ten', 'hundred', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 
    ]
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
    return [0, 1, 10] + [10**i for i in range(3, 13, 3)]


def get_name(number, base):
    return None

def say(number):
    if number == 0:
        return 'zero'
    if number < 100:
        return prehandred_name(number)

    return ''
