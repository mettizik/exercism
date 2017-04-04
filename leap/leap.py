def is_multiple_of(tested, base):
    return (tested % base) == 0

def is_leap_year(tested_year):
    return is_multiple_of(tested_year, 400) or (is_multiple_of(tested_year, 4) and not is_multiple_of(tested_year, 100))