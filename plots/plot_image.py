from pathlib import Path

import matplotlib.pyplot as plt

image_paths = [
    f"C:/Users/thiba/OneDrive/Documents/dev_projects/painting-style-transfer/ressources/training/training/Cezanne/{image_id}.jpg"
    for image_id in [215457, 215458, 215459, 215460]
]


def plot_image():
    images = [plt.imread(image_path) for image_path in image_paths]
    fig, ax = plt.subplots(nrows=2, ncols=2)
    ax[0, 0].imshow(images[0])
    ax[0, 1].imshow(images[1])
    ax[1, 0].imshow(images[2])
    ax[1, 1].imshow(images[3])
    plt.show()
