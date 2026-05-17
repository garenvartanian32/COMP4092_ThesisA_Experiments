def concatenate(self, other):
    from imgaug.augmentables.lines import LineString
    if isinstance(other, LineString):
        points = self.points + [self.points[-1], other.points[0]] + other.points[1:]
    elif isinstance(other, (np.ndarray, list, tuple)):
        points = self.points + [self.points[-1]] + list(other)
    else:
        raise ValueError('Unsupported type for concatenation: {}'.format(type(other)))
    return LineString(points, label=self.label)