def plot(self, axis, ith_plot, total_plots, limits):
        print(self.plot_type_str.upper() + " plot")
        print("%5s %9s  %s" % ("id", " #points", "group"))
        for idx, group in enumerate(self.groups):
            print("%5s %9s  %s" % (idx + 1, len(self.groups[group]), group))
        print('')
        datasets = []
        colors = []
        minx = np.inf
        maxx = -np.inf
        for idx, group in enumerate(self.groups):
            x = date2num([logevent.datetime
                          for logevent in self.groups[group]])
            minx = min(minx, min(x))
            maxx = max(maxx, max(x))
            datasets.append(x)
            color, marker = self.color_map(group)
            colors.append(color)
        if total_plots > 1:
            # if more than one plot, move histogram to twin axis on the right
            twin_axis = axis.twinx()
            twin_axis.set_ylabel(self.ylabel)
            axis.set_zorder(twin_axis.get_zorder() + 1)  # put ax ahead of ax2
            axis.patch.set_visible(False)  # hide the 'canvas'
            axis = twin_axis
        n_bins = max(1, int((maxx - minx) * 24. * 60. * 60. / self.bucketsize))
        if n_bins > 1000:
            # warning for too many buckets
            print("warning: %i buckets, will take a while to render. "
                  "consider increasing --bucketsize." % n_bins)
        n, bins, artists = axis.hist(datasets, bins=n_bins, align='mid',
                                     log=self.logscale,
                                     histtype="barstacked"
                                     if self.barstacked else "bar",
                                     color=colors, edgecolor="none",
                                     linewidth=0, alpha=0.8, picker=True,
                                     label=map(str, self.groups.keys()))
        # scale current y-axis to match min and max values
        axis.set_ylim(np.min(n), np.max(n))
        # add meta-data for picking
        if len(self.groups) > 1:
            for g, group in enumerate(self.groups.keys()):
                for i in range(len(artists[g])):
                    artists[g][i]._mt_plot_type = self
                    artists[g][i]._mt_group = group
                    artists[g][i]._mt_n = n[g][i]
                    if self.barstacked:
                        artists[g][i]._mt_n -= (n[g - 1][i] if g > 0 else 0)
                    artists[g][i]._mt_bin = bins[i]
        else:
            for i in range(len(artists)):
                artists[i]._mt_plot_type = self
                artists[i]._mt_group = group
                artists[i]._mt_n = n[i]
                artists[i]._mt_bin = bins[i]
        return artists