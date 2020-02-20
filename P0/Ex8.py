from Seq0 import *
import operator
FOLDER = "/Users/DANIEL REAL/PycharmProjects/2019-2020-PNE-Practices/Session-04 folder/"
FILENAME = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']

print("-----| Exercise 8 |------")

for i in FILENAME:
    DNAFILE = FOLDER + i + ".txt"
    BASE = sorted(seq_count(DNAFILE).items(), key=operator.itemgetter(1))[-1][0]
    print("Gene", i, ": Most frequent Base:", BASE)
