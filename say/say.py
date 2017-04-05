def prehandred_name(index):
    nulls = [
        'zero', 
        'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
        'hundred', 'thousand', 'million', 'billion', 'trillion', 'quadrillion'
    ]
    units = [nulls[0], 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = [nulls[1], 'eleven', 'twelve', 'thirteen'] + [i + 'teen' for i in units[4:]]
    nums = units + teens    
    for i in range(2, 10):
        nums += [nulls[i]] + [nulls[i] + '-' + unit for unit in units[1:]]
        
    return nums[index]

def get_name(number, base):
    return None

def say(number):
    if number < 100:
        return prehandred_name(number)

    return ''
