import cv2 as cv
import numpy as np

# image = cv.imread("./Resources/Photos/cats.jpg")
image = cv.imread("./Resources/Photos/cats 2.jpg")
cv.imshow("Original Image", image)

# What is masking?
# Masking allows us to focus on what we want to focus.

blank = np.zeros(image.shape[:2], dtype=np.uint8)
# cv.imshow("Blank image", blank)

mask = cv.circle(
    blank, (image.shape[1] // 2 + 45, image.shape[0] // 2),
    100, (255, 255, 255), -1)
cv.imshow("Mask", mask)
# We can also use AND, OR or XOR and OTHER to create all sorts of masks
# NOTE: make sure that size of the masked image is same as that of image

masked = cv.bitwise_and(image, image, mask=mask)
# masked2 = cv.bitwise_and(image2, image2, mask=mask)
cv.imshow("Masked Cats", masked)

cv.waitKey(0)
