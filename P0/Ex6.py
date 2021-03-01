import Seq0

GENE_FOLDER = './sequences/'
ID = 'U5.txt'

print('--------|EXERCISE 6|-------')

U5_Seq = Seq0.seq_read_fasta(GENE_FOLDER + ID)[:20]
reversed_U5 = seq_reverse(U5_Seq)

print('Gene U5:')
print('Frag:', U5_Seq)
print('Rev:', reversed_U5)