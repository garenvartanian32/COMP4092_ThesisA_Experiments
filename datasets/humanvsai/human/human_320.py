def getResultsRange(self):
        specs = ResultsRangeDict()
        analysis = self.getAnalysis()
        if not analysis:
            return specs
        result = analysis.getResult()
        if not api.is_floatable(result):
            return specs
        specs.min = specs.max = result
        result = api.to_float(result)
        dup_variation = analysis.getDuplicateVariation()
        dup_variation = api.to_float(dup_variation)
        if not dup_variation:
            return specs
        margin = abs(result) * (dup_variation / 100.0)
        specs.min = str(result - margin)
        specs.max = str(result + margin)
        return specs