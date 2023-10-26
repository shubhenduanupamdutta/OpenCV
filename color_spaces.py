import cv2 as cv
# import matplotlib.pyplot as plt


image = cv.imread("./Resources/Photos/park.jpg")
cv.imshow("Original Image", image)

# Since by default OpenCV reads in BGR, but most of the other library read
# color as RGB, if we plot above image data directly using matplotlib, it will
# show an inverse image.
# plt.imshow(image)

# plt.figure()

# BGR to RGB
rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv.imshow("RGB image", rgb_image)
# plt.imshow(rgb_image)

# Color Space
# Basically a system of representing color on pixels eg. RGB, GRAYSCALE

# Converting image from BGR (default) to Grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

# BGR to HSV (Hue Saturation Value)
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("HSV version", hsv)

# BGR to L*a*b
lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
cv.imshow("LAB Version", lab)


# We can convert in reverse also similarly, i.e. grayscale to bgr, hsv to bgr
# lab to bgr. But a important note.. you can't convert directly (hsv -> lab) or
# (grayscale -> lab) etc.

cv.waitKey(0)
