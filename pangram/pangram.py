from string import ascii_lowercase

def is_pangram(data):
    alphabet = set(ascii_lowercase)
    dataset = set(data.lower())
    return len(alphabet - dataset) == 0
