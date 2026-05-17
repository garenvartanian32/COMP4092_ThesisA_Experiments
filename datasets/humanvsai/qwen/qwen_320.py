def getResultsRange(self):
    result = self.result
    duplicate_variation = self.duplicate_variation
    parent_result = self.parent_analysis.result
    margin_of_error = duplicate_variation / 100 * parent_result
    min_range = parent_result - margin_of_error
    max_range = parent_result + margin_of_error
    return {'min': min_range, 'max': max_range}