def is_anagrammers(lhs: str, rhs: str):
    rhsd = [ch for ch in rhs]
    try:
        for ch in lhs:
            del rhsd[rhsd.index(ch)]

        return len(rhsd) == 0
    except ValueError:
        return False

def remove_case_duplicates(case_sensitive, case_insensitive):
    lower_sensed = [ item.lower() for item in case_sensitive ]
    return case_sensitive + [ item for item in case_insensitive if item.lower() not in lower_sensed ]

def detect_anagrams(word, candidates):
    annagrams_cs = [candidate for candidate in candidates if is_anagrammers(word, candidate)]
    annagrams_cis = [candidate for candidate in candidates if is_anagrammers(word.lower(), candidate.lower())]
    annagrams_cs = [a for a in annagrams_cs if a.lower() != word.lower()]
    annagrams_cis = [a for a in annagrams_cis if a.lower() != word.lower()]
    
    return remove_case_duplicates(annagrams_cs, annagrams_cis)