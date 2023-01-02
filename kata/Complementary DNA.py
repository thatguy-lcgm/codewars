"""Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the
 development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of
 the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or
  there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)"""


def DNA_strand(dna):
    d = ''
    for e, c in enumerate(dna):
        if c == 'A':
            d += 'T'
        elif c == 'T':
            d += 'A'
        elif c == 'C':
            d += 'G'
        elif c == 'G':
            d += 'C'
    return d


print(DNA_strand("AAAA"), "\033[31mTTTT\033[m")