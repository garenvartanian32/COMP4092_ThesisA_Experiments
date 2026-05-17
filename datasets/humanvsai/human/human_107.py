def concatenate(self, other):
        if not isinstance(other, LineString):
            other = LineString(other)
        return self.deepcopy(
            coords=np.concatenate([self.coords, other.coords], axis=0))