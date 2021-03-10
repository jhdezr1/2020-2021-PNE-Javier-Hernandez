from Seq1 import Seq, test_sequences

def print_result(i, sequence):
    print('Sequence' + str(i) + ': (Length:' + str(sequence.len()) + ') ' + str(sequence))
    a, c, t, g = sequence.count_base()
    print('Bases:', sequence.count())


print('-----|Practice 1, Exercise 6|-----')
#We create the test sequences
list_seq = list(test_sequences())
for i in range(0, len(list_seq)):
    print_result(i, list_seq[i])


