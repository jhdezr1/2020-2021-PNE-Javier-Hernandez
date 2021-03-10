import termcolor

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases = 'NULL'):
        #Initialize the sequence with the value passed as argument when creating the object
        #If Attribute Error: 'Seq' obj has no attribute 'strbases', add self.strbases = strbases at the beginning of the def __init__
        self.strbases = strbases
        if strbases == 'NULL':
            print('Null seq created')
            self.strbases = strbases
        else:
            if self.is_valid_sequence():
                self.strbases = strbases
                print('New sequence created!')

            else:
                self.strbases = 'Error'
                print('INCORRECT sequence detected')
    def is_valid_sequence(self):
        for i in self.strbases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False
        return True

    @staticmethod
    def is_valid_sequence_2(bases):
        for i in strbases:
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

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    super().__init__(strbases)  #
    self.name = name
    print('New gene created')


    def __str__(self):
        """Print the gene name along with the sequence"""
        return self.name + "-" + self.strbases


    def len(self):
        """Calculate the length of the sequence and print the sequence as  well"""
        if len(self.strbases) < 10:
            return "Sequence" + self.strbases + "is not long"
        else:
            return "Sequence" + self.strbases + "is long"

    
# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")