from Seq1 import Seq

def print_result(i, sequence):
    print('Sequence ' + str(1) + ': (Length ' + str(sequence.len()) + ' ) ' + str(sequence))
    print('Bases:', sequence.count())
    print('Rev:', sequence.reverse())
    print('Comp: ', sequence.complement())

# como se accedia a otro directorio ??
PROJECT_PATH = '../P0/sequences/'

print('-----| Practice 1, Exercise 10|------')
s1 = Seq()
s1.read_fasta(PROJECT_PATH + 'ADA.txt')
print('Gene', 'ADA.txt', ': Most frequent Base:', Seq.frequent_base(s1))