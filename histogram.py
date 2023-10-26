import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# NOTE: Histograms allow us to visualize intensity distribution in an image.

image = cv.imread("./Resources/Photos/cats 2.jpg")
cv.imshow("Original Image", image)

# Create a blank image to create a mask
blank = np.zeros(image.shape[:2], dtype=np.uint8)


# Histogram of grayscale image
# First covert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

# Create a mask
mask = cv.circle(blank.copy(), (image.shape[1] // 2, image.shape[0] // 2),
                 100, (255, 255, 255), -1)
# cv.imshow("Mask", mask)

masked_image = cv.bitwise_and(gray, gray, mask=mask)
# cv.imshow("Masked Grayscale image", masked_image)

# Grayscale histogram
gray_hist = cv.calcHist(images=[gray], channels=[
                        0], mask=mask, histSize=[256], ranges=[0, 255])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
