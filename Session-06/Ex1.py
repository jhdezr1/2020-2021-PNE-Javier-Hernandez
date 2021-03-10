class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.is_valid_sequence():
            self.strbases = strbases
            print('New sequence created!')
        else:
            self.strbases = 'Error'
            print('INCORRECT sequence detected')

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != 'A' and c!= 'C' and c != 'G' and c != 'T':
                return False
        return True

    @staticmethod
    def static_function():
        pass

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")