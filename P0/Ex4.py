from Seq0 import *

FOLDER = "/home/alumnos/dreal/PycharmProjects/2019-2020-PNE-Practices/Session-04 folder/"

FILENAME = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']
print("-----| Exercise 4 |------")
BASE = ['A', 'C', 'T', 'G']
for i in FILENAME:
    DNAFILE = FOLDER + i + '.txt'
    print('Gene', i, ':')
    for j in BASE:
        print(j, ': ', seq_count_base(DNAFILE, j))
