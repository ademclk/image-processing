from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np
from Homeworks.convolution import convolution

images = []


def robert_cross(image, gx, gy):

    imgrc_x = convolution(image, gx)
    plt.imshow(imgrc_x, cmap="gray")
    plt.title("Robert Cross // Horizontal Filter Gx")
    plt.show()
    images.append(imgrc_x)

    imgrc_y = convolution(image, gy)
    plt.imshow(imgrc_y, cmap="gray")
    plt.title("Robert Cross // Vertical Filter Gy")
    plt.show()
    images.append(imgrc_y)


def prewitt(image, gx, gy):

    imgp_x = convolution(image, gx)
    plt.imshow(imgp_x, cmap="gray")
    plt.title("Prewitt // Horizontal Filter Gx")
    plt.show()
    images.append(imgp_x)

    imgp_y = convolution(image, gy)
    plt.imshow(imgp_y, cmap="gray")
    plt.title("Prewitt // Vertical Filter Gy")
    plt.show()
    images.append(imgp_y)


def sobel(image, gx, gy):

    img_x = convolution(image, gx)
    plt.imshow(img_x, cmap="gray")
    plt.title("Sobel // Horizontal Filter Gx")
    plt.show()
    images.append(img_x)

    img_y = convolution(image, gy)
    plt.imshow(img_y, cmap="gray")
    plt.title("Sobel // Vertical Filter Gy")
    plt.show()
    images.append(img_y)


h_sobel_filter = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])
v_sobel_filter = np.array([[1, 2, 1],
                           [0, 0, 0],
                           [-1, -2, -1]])

h_prewitt_filter = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])
v_prewitt_filter = np.array([[1, 1, 1],
                             [0, 0, 0],
                             [-1, -1, -1]])

h_rcross_filter = np.array([[1, 0],
                            [0, -1]])
v_rcross_filter = np.array([[0, 1],
                            [-1, 0]])


img = cv2.imread("../Pictures/picture3.jpg")

sobel(img, h_sobel_filter, v_sobel_filter)
prewitt(img, h_prewitt_filter, v_prewitt_filter)
robert_cross(img, h_rcross_filter, v_rcross_filter)

row1 = np.hstack((images[0], images[1]))
row2 = np.hstack((images[0], images[1]))
row3 = np.hstack((images[0], images[1]))

table = np.vstack((row1, row2, row3))

plt.imshow(table, cmap="gray")
plt.title("Robert Cross, Prewitt, Sobel // Comparison")
plt.show()
