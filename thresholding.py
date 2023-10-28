import cv2 as cv

# Thresholding is basically binarisation of an image
# We want to convert an image to black and white, 0 or 1 (255)

# First convert the image into grayscale
image = cv.imread("./Resources/Photos/cats.jpg")

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholded Image", thresh)

# inverse thresholding
threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Inverse Thresholding", thresh_inverse)

# Adaptive thresholding -> we allow computer to decide threshold value
# C = subtracted from mean to adjust our thresholding
adaptive = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive", adaptive)

# You can also use cv.ADAPTIVE_GAUSSIAN... to calculate adaptive


cv.waitKey(0)
