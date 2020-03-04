from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.172"
PORT = 8081

FOLDER = "../Session-04 folder/"
txt = ".txt"
gene = "U5"

FILENAME = FOLDER + gene + txt
s0 = Seq('')
s0 = str(s0.read_fasta(FILENAME))

# -- Create a client object
c = Client(IP, PORT)

c.debug_talk(f"Sending {gene} to the server")
c.debug_talk(s0)
