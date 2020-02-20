from Seq0 import *

FOLDER = "/Users/DANIEL REAL/PycharmProjects/2019-2020-PNE-Practices/Session-04 folder/"

FILENAME = 'U5.txt'

DNAFILE = FOLDER + FILENAME

print("-----| Exercise 6 |------")
print("Gene U5:")
print("Frag:", seq_reverse(DNAFILE)[0])
print("Rev:", seq_reverse(DNAFILE)[1])
