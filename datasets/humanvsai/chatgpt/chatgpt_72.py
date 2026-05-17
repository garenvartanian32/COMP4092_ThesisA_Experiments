from Bio import SeqIO

def write_dna_to_file(dna, path):
    SeqIO.write(dna, path, "fasta")
