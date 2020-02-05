dna_sequence = str(input("Enter a DNA sequence:  "))
total_lenght = 0
A = 0
C = 0
G = 0
T = 0

for index in dna_sequence:
    if index == "A":
        A += 1
    elif index == "C":
        C += 1
    elif index == "G":
        G += 1
    elif index == "T":
        T += 1
    total_lenght += 1

print("Total lenght: ", total_lenght, "\nA:", A, "\nC:", C, "\nG:", G, "\nT:", T)
