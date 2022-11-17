from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np
import random


def show_diff(img1, img2):
    plt.imshow(np.hstack((img1, img2)), cmap="gray")
    plt.show()


def add_noise(image):
    row, col = image.shape
    number_of_pixels = random.randint(1000, 10000)
    for i in range(number_of_pixels):
        y_axis = random.randint(0, row - 1)
        x_axis = random.randint(0, col - 1)
        image[y_axis][x_axis] = 255
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_axis = random.randint(0, row - 1)
        x_axis = random.randint(0, col - 1)
        image[y_axis][x_axis] = 0
    return image


img = cv2.imread('../Pictures/picture3.jpg', 0)
plt.hist(img)
plt.title("Original image")
plt.show()

noisy_image = add_noise(img)

plt.hist(noisy_image)
plt.title("Noisy image")
plt.show()
