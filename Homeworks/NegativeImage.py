from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np


def convert_negative(image):
    l_value = np.max(image)
    negative_image = l_value - image
    return negative_image


# 0 parameter will make it with no color channels. Black&White, only.
img = cv2.imread('../Pictures/picture3.jpg', 0)
print(img.shape)

cv2.imshow("image1", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

negative_img = convert_negative(img)

show_diff = np.vstack((img, negative_img))

print("Original image: ", img.shape)
print("Negative image: ", negative_img.shape)
print("Stacked image: ", show_diff.shape)

plt.imshow(show_diff, cmap="gray")
plt.show()
