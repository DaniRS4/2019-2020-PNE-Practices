from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.253.128"
PORT0 = 8080
PORT1 = 8081
c0 = Client(IP, PORT0)
c1 = Client(IP, PORT1)
FOLDER = "../Session-04 folder/"
txt = ".txt"
gene = "FRAT1"
file_name = FOLDER + gene + txt
s0 = Seq('')
s0 = str(s0.read_fasta(file_name))
len0 = 10
num_frag = 10
print(f"Gene {gene}: {s0}")
for e in range(num_frag):
    print(f"fragment {e+1}: {s0[len0*e:len0*(e+1)]}")
    if (e+1)%2 == 0:
        c1.talk(f"fragment {e + 1}: {s0[len0*e:len0*(e + 1)]}")
    else:
        c0.talk(f"fragment {e+1}: {s0[len0*e:len0*(e+1)]}")