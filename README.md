# Painting style transfer

### Project goal

This project aims at extracting the style from a painting and apply it to pictures. The extracted style will act as a filter, like the one you can commonly use on social media.


### Reference study

The project is based on a study called _A Neural Algorithm of Artistic Style_, led by Leon Gatys, Alexandre Ecker and Matthias Bethge, researchers from the University of Tübingen in Germany.

Link : https://arxiv.org/pdf/1508.06576.pdf

### Dataset

The dataset used from this project was taken from kaggle.com : it contains multiple impressionists paintings scrapped on WikiArt.


Link : https://www.kaggle.com/delayedkarma/impressionist-classifier-data

The dataset is composed of multiple pictures of 10 famous painters paintings. They are in JPG format. The first step is to visualize them.
For this, one should convert the JPG files into numpy arrays, data structure that Python can easily handle.

### Methods

The first idea is to implement a CNN model to extract the style of a painting.
The model will be trained on 10 famous painters artwork in order to extract the 10 corresponding styles.
The second part will consist of applying this style to a picture of a day-to-day moment.

