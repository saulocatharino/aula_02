import numpy as np
import cv2
import matplotlib.pyplot as plt


def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.114])


image = cv2.imread("imagem_4.jpg")

gray = rgb2gray(image)
gray_invert = np.invert(gray.astype(np.int))

if __name__ == "__main__":
     plt.imshow(gray_invert, cmap="Greys")
     plt.show()




