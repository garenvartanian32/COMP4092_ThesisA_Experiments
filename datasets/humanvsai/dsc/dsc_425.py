class FeatureExtractor:
    def __init__(self, features):
        self.features = features

    def get_feature_from_key(self, feature_key):
        if feature_key in self.features:
            return self.features[feature_key]
        else:
            return None