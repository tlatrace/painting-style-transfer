from PIL import Image

image_path = "C:/Users/thiba/OneDrive/Documents/dev_projects/painting-style-transfer/ressources/training/training/Cezanne/215457.jpg"


def get_image_dimensions(image_path):
    image = Image.open(image_path)
    return image.size
