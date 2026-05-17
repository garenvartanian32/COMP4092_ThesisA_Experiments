from PIL import Image, ImageDraw

def draw_cross(position, color, radius):
    image_size = 2*radius + 1
    canvas = Image.new('RGB', (image_size, image_size), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    draw.line((0, radius, image_size, radius), fill=color, width=1)
    draw.line((radius, 0, radius, image_size), fill=color, width=1)
    return canvas
