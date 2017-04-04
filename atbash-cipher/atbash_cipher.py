import string

direct = string.ascii_lowercase
backw = string.ascii_lowercase[-1:0:-1] + string.ascii_lowercase[0]

def encode(data):
    data = data.lower()
    encoded = ''
    for ch in data:
        if ch.isalpha():
            encoded += backw[direct.index(ch)]
        elif ch.isnumeric():
            encoded += ch
    
    return encoded

def decode(data):
    data = data.lower()
    decoded = ''
    for ch in data:
        if ch.isalpha():
            decoded += direct[backw.index(ch)]
        elif ch.isnumeric():
            decoded += ch
    
    return decoded
