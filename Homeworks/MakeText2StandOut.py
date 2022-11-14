from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('../Pictures/newspaper.png', 0)

ret, thresh1 = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)

show_diff = np.hstack((img, thresh1))

plt.imshow(show_diff, cmap="gray")
plt.show()
