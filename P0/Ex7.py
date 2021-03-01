import Seq0

GENE_FOLDER = './sequences/'
ID = 'U5.txt'

print('--------|EXERCISE 7|-------')

U5_Seq = Seq0.seq_read_fasta(GENE_FOLDER + ID)[:20]
complemented_U5 = Seq0.seq_complement(U5_Seq)

print('Gene U5:')
print('Frag:', U5_Seq)
print('complement:', complemented_U5)