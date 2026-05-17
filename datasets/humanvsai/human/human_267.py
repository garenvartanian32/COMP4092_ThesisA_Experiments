def range(cls, dataset, dimension):
        dim = dataset.get_dimension(dimension, strict=True)
        values = dataset.dimension_values(dim.name, False)
        return (np.nanmin(values), np.nanmax(values))