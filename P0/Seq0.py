def seq_ping():
    print("OK!")


def seq_read_fasta(filename):
    bodystr = ""
    file_contents = Path(filename).read_text()
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")
    return (bodystr[0:20])

