import matplotlib.pyplot as plt

image_path = "C:/Users/thiba/OneDrive/Documents/dev_projects/painting-style-transfer/archive/training/training/Cezanne/215457.jpg"


def plot_image():
    image = plt.imread(fpath=image_path)
    fig, ax = plt.subplots()
    ax.imshow(image)
    plt.show()


plot_image()
