import termcolor

class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = 'NULL'
    INVALID_SEQUENCE = 'ERROR'

    def __init__(self, strbases = NULL_SEQUENCE):
        #Initialize the sequence with the value passed as argument when creating the object
        #If Attribute Error: 'Seq' obj has no attribute 'strbases', add self.strbases = strbases at the beginning of the def __init__
        self.strbases = strbases
        strbases = self.strbases
        if strbases == Seq.NULL_SEQUENCE:
            print('Null seq created')
            self.strbases = strbases
        else:
            if self.is_valid_sequence():
                self.strbases = strbases
                print('New sequence created!')

            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print('INCORRECT sequence detected')

    @staticmethod
    def is_valid_sequence_2(bases):
        for i in bases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False
        return True

    def is_valid_sequence(self):
        for i in self.strbases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False
        return True


    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            #in order to use termcolor, we need to pass the first argument(text) as a whole string, the second argument would be the color we want to use
            text = 'Sequence' + str(i) + ': (Length:' + str(list_sequences[i].len()) + ')'+ str(list_sequences[i])
            termcolor.cprint(text, 'yellow')
    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == 'NULL' or self.strbases == 'Error':
            return 0
        else:
            return len(self.strbases)

    def count_base(self):
        A, C, T, G = 0, 0, 0, 0
        total = 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return A, C, G, T
        else:
            for e in self.strbases:
                if e == 'A':
                    A += 1
                elif e == 'C':
                    C += 1
                elif e == 'T':
                    T += 1
                elif e == 'G':
                    G += 1
                total += 1
            return A, C, T, G

    def count(self):
        a, c, g, t = self.count_base()
        return {'A': a, 'C': c, 'G': g, 'T': t}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            return self.strbases[::-1]

def test_sequences():
    s1 = Seq()
    s2 = Seq('ACTGA')
    s3 = Seq('Invalid Sequence')

    return s1, s2, s3
