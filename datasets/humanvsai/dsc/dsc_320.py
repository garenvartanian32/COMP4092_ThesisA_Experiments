def getResultsRange(self):
    # Calculate the margin of error
    margin_of_error = self.result * (self.variation / 100)

    # Calculate the minimum and maximum valid results
    min_result = self.result - margin_of_error
    max_result = self.result + margin_of_error

    # Return the results as a dictionary
    return {'min': min_result, 'max': max_result}