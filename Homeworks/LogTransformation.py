from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np


def log_transform(r, c):
    r = r.astype(float)
    s = c*np.log(1 + r)
    return s.astype(np.uint8)


def re_scale(image):
    s = image.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)


# 0 parameter will make it with no color channels. Black&White, only.
img = cv2.imread('../Pictures/picture3.jpg', 0)
print(img.shape, img.dtype)

log_image = log_transform(img, c=1)

print("Before rescale")
print("Log min: ", np.min(log_image))
print("Log max: ", np.max(log_image))

# Without rescaling, it is just black at least for humans.
log_image = re_scale(log_image)

print("After rescale")
print("Log min: ", np.min(log_image))
print("Log max: ", np.max(log_image))

show_diff = np.vstack((img, log_image))

print("Original image: ", img.shape)
print("Log image: ", log_image.shape)
print("Stacked image: ", show_diff.shape)

plt.imshow(show_diff, cmap="gray")
plt.show()


