from Seq0 import *

FOLDER = "/Users/DANIEL REAL/PycharmProjects/2019-2020-PNE-Practices/Session-04 folder/"

FILENAME = 'U5.txt'

DNAFILE = FOLDER + FILENAME

print("-----| Exercise 7 |------")
print("Gene U5:")
print("Frag:", seq_complement(DNAFILE)[0][0:20])
print("Comp:", seq_complement(DNAFILE)[1][0:20])
