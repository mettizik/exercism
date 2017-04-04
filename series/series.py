def slices(data, slice_size):
    if slice_size <= 0:
        raise ValueError('Invalid slice size passed {}'.format(slice_size))
    
    if slice_size > len(data):
        raise ValueError('Slice size ({}) is bigger than sequence length ({})'.format(slice_size, len(data)))
    
    offset = 0
    retvals = []
    while offset + slice_size <= len(data):
        retvals.append([int(c) for c in data[offset:offset + slice_size]])
        offset += 1

    return retvals
