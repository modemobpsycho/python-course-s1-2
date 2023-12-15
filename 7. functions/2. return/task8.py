def count_AGTC(dna):
    A = dna.count('A')
    G = dna.count('G')
    T = dna.count('T')
    C = dna.count('C')
    return A, G, T, C


assert count_AGTC('AGGTC') == (1, 2, 1, 1)
assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
assert count_AGTC('CCT') == (0, 0, 1, 2)
print('Проверки пройдены')
