def translate(dnaseq,host='human',fmtout=str,tax_id=None):
    if isinstance(dnaseq,str): 
        dnaseq=Seq.Seq(dnaseq,Alphabet.generic_dna)
    if tax_id is None:
        tax_id=1 # stanndard codon table. ref http: 
    prtseq=dnaseq.translate(table=tax_id)
    if fmtout is str:
        return str(prtseq)
    else:
        return prtseq