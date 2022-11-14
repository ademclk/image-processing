from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np


def gama_transform(image, value):
    s = np.array(255*(image/255)**value)
    return s.astype(np.uint8)


# 0 parameter will make it with no color channels. Black&White, only.
img = cv2.imread('../Pictures/picture3.jpg', 0)
print(img.shape, img.dtype)

gama_adjusted_image = gama_transform(img, 2.8)

show_diff = np.vstack((img, gama_adjusted_image))

plt.imshow(show_diff, cmap="gray")
plt.show()
