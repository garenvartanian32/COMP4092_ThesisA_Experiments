def get_average_record(self, n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if len(self) < n:
        raise ValueError("n must be less than or equal to the length of the list")

    averages = []
    for i in range(len(self) - n + 1):
        averages.append(sum(self[i:i+n]) / n)
    return averages