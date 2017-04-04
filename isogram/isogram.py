def is_repeated(data, index, skip_non_char=True):
    if skip_non_char and not data[index].isalpha():
        return False
    
    return data[index] in (data[:index] + data[index + 1:])

def is_isogram(data):
    testedData = data.lower()
    for i in range(len(testedData)):
        if is_repeated(testedData, i):
            return False

    return True
