import re
from operator import mul as multiply
from functools import reduce as accumulate

def validate_product(func):
    def wrapper(numberstr, maxlen):
        if not re.match('^\d+$', numberstr):
            raise ValueError('{} is not a valid number'.format(numberstr))
        return func(numberstr, maxlen)
    return wrapper

def validate_maxlen(func):
    def wrapper(numberstr, maxlen):
        if maxlen > len(numberstr) or maxlen < 0:
            raise ValueError('Invalid maxlen  specified')
        if maxlen == 0:        
            return 1
        return func(numberstr, maxlen)
    return wrapper

@validate_maxlen
@validate_product
def largest_product(numberstr, maxlen):
    vals = []
    for chunk in [ 
        numberstr[i:i + maxlen] for i in range(len(numberstr) - maxlen + 1) 
        ]:
        vals.append(accumulate(multiply, [int(n) for n in chunk]))
        
    return max(vals)
