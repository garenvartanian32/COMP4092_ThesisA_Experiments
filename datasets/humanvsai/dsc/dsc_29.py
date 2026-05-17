import numpy as np

def _jitter(c, magnitude):
    """Replace pixels by random neighbors at `magnitude`."""
    # Get the shape of the image
    height, width, channels = c.shape

    # Create a grid of random indices
    rand_indices = np.random.randint(0, magnitude, size=(height, width, channels))

    # Replace pixels by random neighbors
    for i in range(height):
        for j in range(width):
            for k in range(channels):
                c[i, j, k] = c[rand_indices[i, j, k], rand_indices[i, j, k], k]

    return c