def summarize_evidence(locus, score=lambda pileup: len(pileup)):
    allele_pileups = locus.pileups.group_by_allele()
    evidence_summary = []
    for allele, pileup in allele_pileups.items():
        score_value = score(pileup)
        evidence_summary.append((allele, score_value))
    return evidence_summary