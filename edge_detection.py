import cv2 as cv
import numpy as np

image = cv.imread("./Resources/Photos/park.jpg")
# cv.imshow("Original", image)

# Gradients and Edge
# While normally gradients and edges are completely different things, in
# OpenCV we can assume them to be the same

# First conversion to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# Laplacian Edge detection
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.array(np.absolute(lap), dtype=np.uint8)
cv.imshow("Laplacian Edges", lap)

# Soble Gradient Magnitude Representation
# It calculates gradients in two directions
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobel_x, sobel_y)

cv.imshow("Sobel X", sobel_x)
cv.imshow("Sobel Y", sobel_y)
cv.imshow("Sobel Combined", combined_sobel)


# Canny Edge Detection
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)


cv.waitKey(0)
