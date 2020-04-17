import http.client
import json
from termcolor import *
from Seq1 import *

# lists of genes and identifiers.
genes = ['FRAT1', 'ADA', 'FXN', 'RNU6_269P', 'MIR633', 'TTTY4C', 'RBMY2YP', 'FGFR3', 'KDR', 'ANK2']
identifiers = ['ENSG00000165879', 'ENSG00000196839', 'ENSG00000165060', 'ENSG00000212379', 'ENSG00000207552', 'ENSG00000228296', 'ENSG00000227633', 'ENSG00000068078', 'ENSG00000128052', 'ENSG00000145362']

# Dictionary of both lists genes and identifiers.
dict_genes = dict(zip(genes, identifiers))

# Types of bases.
bases = ["A", "C", "T", "G"]

for i in genes:

    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/sequence/id/'
    PARAMS = dict_genes[i] + '?content-type=application/json'
    URL = SERVER + ENDPOINT + PARAMS
    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMS)

    except ConnectionRefusedError:
        print("ERROR!!")

    resp1 = conn.getresponse()

    print(f"Response received!: {resp1.status} {resp1.reason}")

    data_read = resp1.read().decode("utf-8")

    api_info = json.loads(data_read)
    colored_gene = colored("Gene", 'green')
    print(f"{colored_gene}: {i}")

    colored_desc = colored("Description", 'green')
    print(f"{colored_desc}: {api_info['desc']}")

    seq0 = Seq(api_info['seq'])
    colored_len = colored("Total length", 'green')
    print(f"{colored_len}: {seq0.len()}")

    most_frequent_Base = []
    for e in bases:
        e = colored(e, 'blue')
        print(f"{e} : {seq0.count_base(e)} ({round(seq0.count_base(e) * (100 / seq0.len()), 2)}%)")

    most_frequent_color = colored(f"Most frequent base", 'green')
    val = 0
    base = ''
    for i, t in (seq0.count()).items():
        while t > val:
            val = t
            base = i
    print(f"{most_frequent_color}: {base}")
