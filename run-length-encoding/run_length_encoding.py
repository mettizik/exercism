def get_number_head(input_data):
    strnum = ''
    counter = 0
    for ch in input_data:
        if ch.isnumeric():
            strnum += ch
            counter += 1
        else:
            break

    return int(strnum), counter


def decode(input_data):
    output_data = ''
    index = 0
    while index < len(input_data):
        ch = input_data[index]
        if ch.isnumeric():
            count, index_delta = get_number_head(input_data[index:])
            index += index_delta
            output_data += input_data[index] * count
            
        else:
            output_data += ch

        index += 1

    return output_data

def get_repeated(input_data):
    starter = input_data[0]
    counter = 1
    for ch in input_data[1:]:
        if ch == starter:
            counter += 1
        else:
            break
    
    return starter, counter

def encode(input_data):
    output_data = ''
    index = 0
    while index < len(input_data):
        ch, count = get_repeated(input_data[index:])
        index += count
        if count == 1:
            output_data += ch

        else:
            output_data += str(count) + ch

    return output_data
