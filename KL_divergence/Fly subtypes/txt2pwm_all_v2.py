from Bio import SeqIO
from Bio import motifs
import Bio.Seq
import sys
import argparse
print("#INCLUSive Motif Model")
print("#")

def calc(fn):
    all_motifs = []
    with open(fn) as input:
        for line in input.readlines():
            if line:
                if "N" in line:
                    continue
                seq = Bio.Seq.Seq(str(line.strip()[11-4: 16]))
                all_motifs.append(seq)
    m = motifs.create(all_motifs)

    print("#ID = {}".format(fn))
    print("#W = 9")
    for A, C, G, T in zip(*[m.pwm["A"], m.pwm["C"], m.pwm["G"], m.pwm["T"]]):
        print("{}\t{}\t{}\t{}".format(A, C, G, T))
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","-input",dest="input",required=True,help="", nargs="*")
    options = parser.parse_args()
    for f in options.input:
        calc(f)