def get_feature_from_key(self, feature_key):
    feature = self.features.get(feature_key, None)
    if feature is None:
        raise KeyError(f"Feature with key '{feature_key}' not found.")
    return feature