import re

def word_count(sentence):
    ret = {}
    for word in re.split('[\W_]+', sentence.lower()):
        if len(word) == 0:
            continue
        if word not in ret:
            ret[word] = 1
        else:
            ret[word] += 1

    return ret