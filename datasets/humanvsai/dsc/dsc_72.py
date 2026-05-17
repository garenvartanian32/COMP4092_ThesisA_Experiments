import os

def write_dna(dna, path):
    """Write DNA to a file (genbank or fasta).

    :param dna: DNA sequence to write to file
    :type dna: coral.DNA
    :param path: file path to write. Has to be genbank or fasta file.
    :type path: str"""

    # Check if the file path is valid
    if not os.path.exists(os.path.dirname(path)):
        raise ValueError("Invalid file path.")

    # Check if the file path ends with .gbk or .fasta
    if not path.endswith(".gbk") and not path.endswith(".fasta"):
        raise ValueError("File path must end with .gbk or .fasta.")

    # Write the DNA sequence to the file
    with open(path, "w") as file:
        file.write(dna)