from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.253.128"
PORT = 8080
c = Client(IP, PORT)
FOLDER = "../Session-04 folder/"
txt = ".txt"
gene = "FRAT1"
file_name = FOLDER + gene + txt
s0 = Seq('')
s0 = str(s0.read_fasta(file_name))
len0 = 10
num_frag = 5
print(f"Gene {gene}: {s0}")
for e in range(num_frag):
    print(f"fragment {e+1}: {s0[len0*e:len0*(e+1)]}")
    c.talk(f"fragment {e+1}: {s0[len0*e:len0*(e+1)]}")