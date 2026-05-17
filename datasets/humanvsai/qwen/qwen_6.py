def get_average_record(self, n):
    averages = []
    for i in range(n, len(self.data) + 1):
        average = sum(self.data[i - n:i]) / n
        averages.append(average)
    return averages