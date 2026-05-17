def write_dna(dna, path):
    # Check if path filetype is valid, remember for later
    ext = os.path.splitext(path)[1]
    if ext == '.gb' or ext == '.ape':
        filetype = 'genbank'
    elif ext == '.fa' or ext == '.fasta':
        filetype = 'fasta'
    else:
        raise ValueError('Only genbank or fasta files are supported.')
    # Convert features to Biopython form
    # Information lost on conversion:
    #     specificity of feature type
    #     strandedness
    #     topology
    features = []
    for feature in dna.features:
        features.append(_coral_to_seqfeature(feature))
    # Biopython doesn't like 'None' here
    # FIXME: this is a legacy feature - remove?
    bio_id = dna.id if hasattr(dna, 'id') else ''
    # Maximum length of name is 16
    seq = SeqRecord(Seq(str(dna), alphabet=ambiguous_dna), id=bio_id,
                    name=dna.name[0:16].replace(' ', '_'), features=features,
                    description=dna.name)
    if dna.circular:
        seq.annotations['data_file_division'] = 'circular'
    else:
        seq.annotations['data_file_division'] = 'linear'
    if filetype == 'genbank':
        SeqIO.write(seq, path, 'genbank')
    elif filetype == 'fasta':
        SeqIO.write(seq, path, 'fasta')