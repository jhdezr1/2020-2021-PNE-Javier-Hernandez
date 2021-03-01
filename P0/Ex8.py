import Seq0
GENE_FOLDER = './sequences/'
gene_list = ['U5', 'ADA', 'FRAT1', 'FXN']
print('-----------|EXERCISE 8|--------')

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt')
    A, C, G, T = sequence.count('A'), sequence.count('C'), sequence.count('G'), sequence.count('T')

    if A >= C and A >=G and A >= T:
        print ('Gene ', gene, ': Most frequent Base is A')
    elif C >= A and C >= G and C >= T:
        print('Gene ', gene, ': Most frequent Base is C')
    elif G >= A and G >= C and G >= T:
        print('Gene ', gene, ': Most frequent Base is G')
    elif T >= A and T >= C and T >= G:
        print('Gene ', gene, ': Most frequent Base is T')
    else:
        print('Gene ', gene, ': Most frequent Base is 0')