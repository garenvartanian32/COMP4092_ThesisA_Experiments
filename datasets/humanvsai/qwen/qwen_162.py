def _sprite_url(map):
    return f'https://example.com/sprite/{map}.png'

def _sprite_coordinates(map, feature):
    """Returns the coordinates of a feature within the sprite image."""
    coordinates = {'map1': {'feature1': (10, 20), 'feature2': (30, 40)}, 'map2': {'feature1': (50, 60), 'feature2': (70, 80)}}
    return coordinates.get(map, {}).get(feature, (0, 0))

def get_sprite_info(map, feature):
    """Returns the sprite URL and coordinates for a given map and feature."""
    url = _sprite_url(map)
    coordinates = _sprite_coordinates(map, feature)
    return (url, coordinates)
map_name = 'map1'
feature_name = 'feature1'
(url, coordinates) = get_sprite_info(map_name, feature_name)