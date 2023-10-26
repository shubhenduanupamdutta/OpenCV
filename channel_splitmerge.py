import cv2 as cv
import numpy as np

image = cv.imread("./Resources/Photos/park.jpg")
cv.imshow("Original Image", image)

# Channels are basically color component of the image, in this case BGR i.e.
# Blue , green and red
# Splitting into channels

# Note: individual channel images are grayscale images, white representing as
# more of that color present, black representing less
b, g, r = cv.split(image)
for i, color in enumerate((b, g, r)):
    color_mapping = {1: "blue", 2: "green", 3: "red"}
    # cv.imshow(f"color: {color_mapping[i + 1]}", color)
    print(color.shape)

# merging the colors back
merged = cv.merge([b, g, r])
cv.imshow("Merged Back Image", merged)

print(image.shape)

# To show individual channel images as color, we can do the following
blank = np.zeros(image.shape[:2], dtype=np.uint8)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

cv.waitKey(0)
