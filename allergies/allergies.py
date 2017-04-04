import math

allergens = [
    'eggs',
    'peanuts', 
    'shellfish', 
    'strawberries',
    'tomatoes',
    'chocolate',
    'pollen',
    'cats'
]

class Allergies(object):
    score_table = dict(zip([2**i for i in range(len(allergens))], allergens))
    def __init__(self, score):
        self.lst = []
        if score > 2**len(allergens):
            score = score % 2**len(allergens)
            
        for key in Allergies.score_table.keys():
            if key == key & score:
                self.lst.append(Allergies.score_table[key])

    def is_allergic_to(self, name):
        return name in self.lst