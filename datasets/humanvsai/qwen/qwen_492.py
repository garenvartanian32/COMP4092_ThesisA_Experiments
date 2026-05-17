def plot(self, axis, ith_plot, total_plots, limits):
    num_bins = int(np.sqrt(len(self.data)))
    data_range = max(self.data) - min(self.data)
    bin_width = data_range / num_bins
    bin_edges = np.linspace(min(self.data), max(self.data), num_bins + 1)
    (counts, _) = np.histogram(self.data, bins=bin_edges)
    counts = counts / len(self.data)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    axis.bar(bin_centers, counts, width=bin_width, align='center', alpha=0.7, color='blue')
    axis.set_xlim(limits[0], limits[1])
    axis.set_xlabel('Value')
    axis.set_ylabel('Normalized Frequency')
    axis.set_title(f'Histogram of Data (Plot {ith_plot} of {total_plots})')