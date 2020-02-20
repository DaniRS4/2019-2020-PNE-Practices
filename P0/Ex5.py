from Seq0 import *

FOLDER = "/Users/DANIEL REAL/PycharmProjects/2019-2020-PNE-Practices/Session-04 folder/"

FILENAME = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']
print("-----| Exercise 5 |------")
BASE = ['A', 'C', 'T', 'G']

for i in FILENAME:
    DNAFILE = FOLDER + i + '.txt'
    print('Gene', i, ': ', seq_count(DNAFILE))
