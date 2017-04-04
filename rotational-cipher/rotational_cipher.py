import string

def get_encoded_char(ch, shifter):    
    cased_chars = string.ascii_uppercase if ch.isupper() else string.ascii_lowercase
    charset = cased_chars + cased_chars
    charindex = ord(ch) + shifter - ord(cased_chars[0])
    if charindex > 25:
        charindex = charindex % 26
    return charset[charindex]

def rotate(data, shifter):
    retval = ''
    for d in data:        
        if d.isalpha():
            retval += get_encoded_char(d, shifter)
        else:
            retval += d

    return retval
