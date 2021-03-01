import Seq0
GENE_FOLDER = './sequences/'
gene_list = ['U5', 'ADA', 'FRAT1', 'FXN']

print('---------|EXERCISE 3|---------')

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt')
    print('Gene ', gene, '---->', Seq0.seq_len(sequence))