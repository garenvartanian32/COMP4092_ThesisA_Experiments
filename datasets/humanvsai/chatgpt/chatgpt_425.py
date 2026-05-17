def get_feature(feature_key):
    features = {
        'feature1': 'This is the feature 1',
        'feature2': 'This is the feature 2',
        'feature3': 'This is the feature 3',
    }
    return features.get(feature_key, 'Feature not found')
