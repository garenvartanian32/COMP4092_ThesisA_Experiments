def write_dna(dna, path):
    import coral
    import os
    (_, ext) = os.path.splitext(path)
    if ext.lower() not in ['.gb', '.gbk', '.fasta', '.fa']:
        raise ValueError('File extension must be .gb, .gbk, .fasta, or .fa')
    if ext.lower() in ['.gb', '.gbk']:
        dna.write_genbank(path)
    elif ext.lower() in ['.fasta', '.fa']:
        dna.write_fasta(path)
    else:
        raise ValueError('Unsupported file format')