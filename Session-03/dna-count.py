def count_base(dna):
    A = 0
    C = 0
    T = 0
    G = 0
    total = 0
    for e in dna:
        if e == 'A':
            A += 1
        elif e == 'C':
            C += 1
        elif e == 'T':
            T += 1
        elif e == 'G':
            G += 1
        total += 1
    return A, C, T, G, total

dna = input('Enter a dna strand ')
count_a, count_c, count_t, count_g, total = count_base(dna)
if total == (count_a + count_c + count_g + count_t):
    print('total length: ', total)
    print('A: ', count_a)
    print('C: ', count_c)
    print('T: ', count_t)
    print('G: ', count_g)
else:
    print('The dna strand is not valid as it contains letters other than A, G, C or T')