def get_feature_from_key(self, feature_key):
    feature = self.feature_key_map.get(feature_key)
    if feature:
      return feature
    self.logger.error('Feature "%s" is not in datafile.' % feature_key)
    return None