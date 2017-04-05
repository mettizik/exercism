import re

def get_acronic(word):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', word)
    subwords = [m.group(0) for m in matches]
    return ''.join([sw[0].upper() for sw in subwords])

def abbreviate(sentence):
    return ''.join([get_acronic(word) for word in re.split('\W+', sentence)])
