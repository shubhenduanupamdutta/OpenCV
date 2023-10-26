import cv2 as cv
import matplotlib.pyplot as plt

# NOTE: Histograms allow us to visualize intensity distribution in an image.

image = cv.imread("./Resources/Photos/cats 2.jpg")
cv.imshow("Original Image", image)

# Histogram of grayscale image
# First covert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

# Grayscale histogram
gray_hist = cv.calcHist(images=[gray], channels=[
                        0], mask=None, histSize=[256], ranges=[0, 255])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
