from Seq1 import Seq

def print_count(a, c, t, g):
    print('A: ' +  str(a) + 'C: ' + str(c) + 'T: ' + str(t) + 'G: ' + str(g))

print('-----|Exercise 5|-----')
s1 = Seq()
s2 = Seq('ACTGA')
s3 = Seq('Invalid Sequence')
print('Sequence' + str(1) + ': (Length:' + str(s1.len()) + ') '+ str(s1))
print_count(s1.count_bases())
print('Sequence' + str(2) + ': (Length:' + str(s2.len()) + ') '+ str(s2))
print('Sequence' + str(3) + ': (Length:' + str(s3.len()) + ') '+ str(s3))