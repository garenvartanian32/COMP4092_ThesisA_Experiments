def filtered_site_collection(indices):
    if set(indices).issubset(set(range(tot_sites))):
        return SiteCollection.filter(indices)
    else:
        return SiteCollection
