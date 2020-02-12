from pathlib import Path

FILENAME = "ADA.txt"

file_contents = Path(FILENAME).read_text()

body = file_contents.split("\n")[1:]
nucleotids = " "
nucleotids = nucleotids.join(body)
nucleotids = nucleotids.replace(" ", "")

print(len(nucleotids))
