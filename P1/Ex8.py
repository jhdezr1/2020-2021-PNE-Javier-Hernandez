from Seq1 import test_sequences

def print_result(i, sequence):
    print('Sequence' + str(i) + ': (Length:' + str(sequence.len()) + ') ' + str(sequence))
    print('Bases:', sequence.count())
    print('Rev:', sequence.reverse())
    print('Complement:', sequence.complement())


print('-----|Practice 1, Exercise 8|-----')
#We create the test sequences
list_seq = list(test_sequences())
for i in range(0, len(list_seq)):
    print_result(i, list_seq[i])