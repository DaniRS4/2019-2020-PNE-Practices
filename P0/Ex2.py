from Seq0 import *

FOLDER = "/home/alumnos/dreal/PycharmProjects/2019-2020-PNE-Practices/Session-04 folder/"

FILENAME = "U5.txt"
DNAFILE = FOLDER + FILENAME

print(DNAFILE)
print("-----| Exercise 2 |------")
print("DNA file: ", FILENAME)
print("The first 20 bases are: ", seq_read_fasta(DNAFILE))
