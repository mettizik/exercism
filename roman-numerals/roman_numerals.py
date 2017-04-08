from math import log10

_mask = {
    0: '',
    1: '0',
    2: '00',
    3: '000',
    4: '01',
    5: '1',
    6: '10',
    7: '100',
    8: '1000',
    9: '02',
    10: '2'
}

_letters = [
    ['I', 'V', 'X'], 
    ['X', 'L', 'C'],
    ['C', 'D', 'M'],
    ['M'] # Dummy letter for numbers from 1999 to 3000
]

def impl(numb, base):
    if base < 1:
        return ''
    digit, rest = divmod(numb, base)    
    letters = _letters[int(log10(base))]
    return ''.join([letters[int(c)] for c in _mask[digit]]) + impl(rest, int(base / 10))

def numeral(numb):
    return impl(numb, 10**int(log10(numb)))
