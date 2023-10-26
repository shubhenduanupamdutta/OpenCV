import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("./Resources/Photos/cats.jpg")
cv.imshow("Original Image", image)

# Blank image
blank = np.zeros(image.shape[:2], dtype=np.uint8)

mask = cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 100,
                 (255, 255, 255), -1)

masked_image = cv.bitwise_and(image, image, mask=mask)
cv.imshow("Masked Image", masked_image)

plt.figure()
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.title("Color  Histogram")
colors = ("b", "g", "r")
for i, color in enumerate(colors):
    hist = cv.calcHist([image], channels=[i], mask=None, histSize=[256],
                       ranges=[0, 255])
    plt.plot(hist, color)
    plt.xlim([0, 256])

plt.figure()
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.title("Color Masked  Histogram")
colors = ("b", "g", "r")
for i, color in enumerate(colors):
    hist = cv.calcHist([image], channels=[i], mask=mask, histSize=[256],
                       ranges=[0, 256])
    plt.plot(hist, color)
    plt.xlim([0, 255])

plt.show()

cv.waitKey(0)
