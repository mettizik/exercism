dna_to_rna = {
'G': 'C',
'C': 'G',
'T': 'A',
'A': 'U'}

def to_rna(dna):
    rna = ''
    try:
        for nuc in dna:
            rna += dna_to_rna[nuc]
    except KeyError:
        return ''

    return rna