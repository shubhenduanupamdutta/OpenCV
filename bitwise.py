import cv2 as cv
import numpy as np


# Bitwise operation is just OR, AND, XOR and NOT commands
# Basically turns pixel on if value is 1, off if pixel is 0
blank = np.zeros((400, 400, 1), dtype=np.uint8)
# We will use this blank as basis of drawing rectangle and circle
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200,
                   (255, 255, 255), thickness=-1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# Bitwise AND
# What it does -> Takes two images, lays it on top of each other, and returns
# the intersection of the images
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# Bitwise OR
# Returns the union of two images
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)

# Bitwise XOR -> Returns only non-intersecting region
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

# Bitwise NOT -> It inverts the binary color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Rectangle NOT", bitwise_not)

cv.waitKey(0)
