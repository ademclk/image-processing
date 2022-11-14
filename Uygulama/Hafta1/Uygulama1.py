import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

print(cv2.__version__)


img1 = cv2.imread("../../Pictures/picture3.jpg", cv2.IMREAD_COLOR)  # 1
img2 = cv2.imread('../../Pictures/picture2.jpg', cv2.IMREAD_GRAYSCALE)  # 0
img3 = cv2.imread('../../Pictures/picture3.jpg', cv2.IMREAD_UNCHANGED)  # -1


# cv2.imread(path, flag),
# Return Value: This method returns an image that is loaded from the specified file.
"""
cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print(img1.shape)
print(img2.shape)
print(img3.shape)

print(img3[10, 10])  # Her piksel değeri de bu 3 ana renk içerir->BGR --Diyelimki sadece kımızı R:255, G:0, B:0

image_rgb = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
print(image_rgb[300, 269])

cv2.imshow('image1', image_rgb)
cv2.waitKey(10000) # ms süresi kadar ekranda kalır. 0 ise süresiz ekranda kalma.
cv2.destroyAllWindows()


arr = np.array(img3)
for i, item in enumerate(arr):
    print(item[0])

methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

for id, interp_method in enumerate(methods):
    plt.imshow(img1, interpolation=interp_method, cmap='gray')
    plt.tight_layout()
    plt.show()

plt.imshow(img1, cmap='viridis', interpolation='bicubic')
plt.show()
plt.close()
