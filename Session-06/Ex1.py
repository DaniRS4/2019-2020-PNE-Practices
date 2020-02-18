class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        bases = []
        for index in strbases:
            if index == "A" or "C" or "G" or "T":
                bases.append[index]
            else:
                print("ERROR")
                break
    print("".join(bases))


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq):

    pass

# -- Main Program
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
