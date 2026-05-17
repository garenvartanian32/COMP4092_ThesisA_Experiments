def get_average_current(data, n):
    averages = []
    for i in range(len(data)):
        if i < n:
            averages.append(sum(data[:i+1]) / (i+1))
        else:
            averages.append(sum(data[i-n+1:i+1]) / n)
    return averages
