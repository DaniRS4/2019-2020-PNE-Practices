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
    base = ['A', 'C', 'T', 'G']
    counter_a = 0
    counter_t = 0
    counter_c = 0
    counter_g = 0
    countlist = []
    for i in seq:
        if i == "A":
            counter_a = counter_a + 1
        elif i == "T":
            counter_t = counter_t + 1
        elif i == "C":
            counter_c = counter_c + 1
        elif i == "G":
            counter_g = counter_g + 1
        else:
            continue
    countlist.append(counter_a)
    countlist.append(counter_t)
    countlist.append(counter_c)
    countlist.append(counter_g)

    basesdict = dict(zip(base, countlist))
    return basesdict


def seq_reverse(filename):
    bodystr = ""
    file_contents = Path(filename).read_text()
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")
    first20 = bodystr[0:20]
    first20reverse = first20[::-1]
    return first20, first20reverse


def seq_complement(filename):
    bodystr = ""
    file_contents = Path(filename).read_text()
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")
    complement = ""
    for i in bodystr:
        if i == "A":
            complement = complement + "T"
        elif i == "C":
            complement = complement + "G"
        elif i == "G":
            complement = complement + "C"
        elif i == "T":
            complement = complement + "A"
        else:
            continue
    return bodystr, complement
