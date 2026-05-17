import random
from PIL import Image

def replace_pixels(image_path, magnitude):
    # Open image and convert to RGB mode
    image = Image.open(image_path).convert('RGB')
    # Get the width and height of the image
    width, height = image.size
    # Create a new blank image of the same size and mode as the original image
    new_image = Image.new(mode='RGB', size=(width, height))
    # Loop over each pixel in the image
    for y in range(height):
        for x in range(width):
            # Get the current pixel from the original image
            current_pixel = image.getpixel((x, y))
            # Choose a random neighbor pixel
            random_neighbor = (
                random.randint(max(x - magnitude, 0), min(x + magnitude, width - 1)),
                random.randint(max(y - magnitude, 0), min(y + magnitude, height - 1))
            )
            # Get the neighbor pixel from the original image
            neighbor_pixel = image.getpixel(random_neighbor)
            # Replace the current pixel with the neighbor pixel
            new_image.putpixel((x, y), neighbor_pixel)
    # Return the new image
    return new_image
