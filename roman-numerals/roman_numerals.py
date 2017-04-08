_mask = {
    0: '',
    1: '*',
    2: '**',
    3: '***',
    4: '*+',
    5: '+',
    6: '+*',
    7: '+**',
    8: '+***',
    9: '*++',
    10: '++'
}

_letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'Z', 'Y']

def numeral(numb):
    if numb < 10:
        letters = _letters[0:3]
        return _mask[numb].replace('++', letters[2]).replace('+', letters[1]).replace('*', letters[0])
    if numb < 100:        
        letters = _letters[2:5]        
        return _mask[int(numb / 10)].replace('++', letters[2]).replace('+', letters[1]).replace('*', letters[0]) + numeral(numb - int(numb / 10) * 10)
    if numb < 1000:
        letters = _letters[4:7]        
        return _mask[int(numb / 100)].replace('++', letters[2]).replace('+', letters[1]).replace('*', letters[0]) + numeral(numb - int(numb / 100) * 100)
    if numb < 10000:
        letters = _letters[6:]        
        return _mask[int(numb / 1000)].replace('++', letters[2]).replace('+', letters[1]).replace('*', letters[0]) + numeral(numb - int(numb / 1000) * 1000)
