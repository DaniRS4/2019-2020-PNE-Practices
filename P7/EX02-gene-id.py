from termcolor import *

# lists of genes and identifiers.
genes = ['FRAT1', 'ADA', 'FXN', 'RNU6_269P', 'MIR633', 'TTTY4C', 'RBMY2YP', 'FGFR3', 'KDR', 'ANK2']
identifiers = ['ENSG00000165879', 'ENSG00000196839', 'ENSG00000165060', 'ENSG00000212379', 'ENSG00000207552', 'ENSG00000228296', 'ENSG00000227633', 'ENSG00000068078', 'ENSG00000128052', 'ENSG00000145362']

# Dictionary of both lists genes and identifiers.
dict_genes = dict(zip(genes, identifiers))

print("Dictionary of Genes!!")
print(f"There are {len(dict_genes)} genes in the dictionary:")

colored_gene = ''
for keys, values in dict_genes.items():
    colored_gene = colored(keys, 'green')
    print(f"{colored_gene}: --> {values}")
