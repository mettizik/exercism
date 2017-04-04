import re

def hey(phrase):
    phrase = phrase.strip()
    if phrase.isupper():
        return 'Whoa, chill out!'
    if re.match('.*\?\s*$', phrase):
        return 'Sure.'
    if re.match('\W*$', phrase):
        return 'Fine. Be that way!'

    return 'Whatever.'