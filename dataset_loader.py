import os
import cv2
import numpy as np

def load_dataset(folder):
    images = []

    for file in os.listdir(folder):
        img_path = os.path.join(folder, file)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (224,224))
        images.append(img)

    return np.array(images)
