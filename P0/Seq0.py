from pathlib import Path


def seq_ping():
    print("OK!")


def seq_read_fasta(filename):
    bodystr = ""
    file_contents = Path(filename).read_text()
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")
    return bodystr[0:20]


def seq_len(seq):
    bodystr = ""
    file_contents = Path(seq).read_text()
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")
    return len(bodystr)


def seq_count_base(seq, base):
    count = 0
    file_contents = Path(seq).read_text()
    seq = ""
    lines = file_contents.split('\n')
    body = lines[1:]
    seq = seq.join(body).replace(" ", "")
    for i in seq:
        if i == base:
            count += 1
    return count


def seq_count(seq):
    file_contents = Path(seq).read_text()
    seq = ""
    lines = file_contents.split('\n')
    body = lines[1:]
    seq = seq.join(body).replace(" ", "")
    BASE = ['A', 'C', 'T', 'G']
    counterA = 0
    counterT = 0
    counterC = 0
    counterG = 0
    countlist = []
    for i in seq:
        if i == "A":
            counterA = counterA + 1
        elif i == "T":
            counterT = counterT + 1
        elif i == "C":
            counterC = counterC + 1
        elif i == "G":
            counterG = counterG + 1
        else:
            next
    countlist.append(counterA)
    countlist.append(counterT)
    countlist.append(counterC)
    countlist.append(counterG)

    basesdict = dict(zip(BASE, countlist))
    return (basesdict)


def seq_reverse(filename):
    bodystr = ""
    file_contents = Path(filename).read_text()
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")
    first20 = bodystr[0:20]
    first20reverb = first20[::-1]
    return (first20, first20reverb)


def seq_complement(seq):
    comp = ""
    for i in seq:
        if i == "A":
            comp = comp + "T"
        elif i == "C":
            comp = comp + "G"
        elif i == "G":
            comp = comp + "C"
        elif i == "T":
            comp = comp + "A"
        else:
            next
    return comp