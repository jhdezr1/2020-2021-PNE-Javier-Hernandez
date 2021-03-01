from pathlib import Path
import operator

def seq_ping():
    print('Ok')

def take_out_first_line(seq):
    return seq[seq.find('\n') + 1:].replace('\n', '')

def seq_read_fasta(filename):
    return take_out_first_line(Path(filename).read_text())

def seq_len(seq):
    return len(seq)

def seq_count_base(sequence, base):
    return sequence.count(base)

def seq_count(sequence):
    a, c, g, t = 0, 0, 0, 0
    for d in sequence:
        if d == 'A':
            a += 1
        elif d == 'C':
            c += 1
        elif d == 'G':
            g += 1
        elif d == 'T':
            t += 1
    return {'A': a, 'C': c, 'G': g, 'T': t}

def seq_reverse(sequence):
    empty = ''
    for e in sequence:
        rever_seq = e + empty
        empty = rever_seq
    return rever_seq
