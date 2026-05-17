def allele_summary(self, locus, score=lambda x: x.num_reads()):
        locus = to_locus(locus)
        return [
            (allele, score(x))
            for (allele, x) in self.group_by_allele(locus).items()
        ]