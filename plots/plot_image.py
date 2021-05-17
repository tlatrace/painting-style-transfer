import os

import matplotlib.pyplot as plt
from utils.image_processing import get_image_dimensions

image_paths = [
    f"C:/Users/thiba/OneDrive/Documents/dev_projects/painting-style-transfer/ressources/training/training/Cezanne/{image_id}.jpg"
    for image_id in [215457, 215458, 215459, 215460]
]
images_directory = "C:/Users/thiba/OneDrive/Documents/dev_projects/painting-style-transfer/ressources/training/training/Cezanne/"


def plot_image(image_paths):
    images = [plt.imread(image_path) for image_path in image_paths]
    fig, ax = plt.subplots(nrows=2, ncols=2)
    ax[0, 0].imshow(images[0])
    ax[0, 1].imshow(images[1])
    ax[1, 0].imshow(images[2])
    ax[1, 1].imshow(images[3])
    plt.show()


def plot_image_dimensions_distribution(images_directory):
    dimensions_list = [
        get_image_dimensions(os.path.join(images_directory, filename))
        for filename in os.listdir(images_directory)
    ]
    x_dimensions = [shape[0] for shape in dimensions_list]
    y_dimensions = [shape[1] for shape in dimensions_list]

    plt.scatter(x_dimensions, y_dimensions)

    plt.title("Image dimensions distribution")
    plt.xlabel("x_pixels_number")
    plt.ylabel("y_pixels_number")
    plt.grid(True, linestyle='--')

    plt.show()


plot_image_dimensions_distribution(images_directory)
