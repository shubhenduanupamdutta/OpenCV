"""
Tutorial and training in OpenCV, computer  vision library.
"""

import cv2 as cv

# Reading and showing images in OpenCV
# image = cv.imread("./Resources/Photos/cat_large.jpg")
# # print(type(image))

# cv.imshow("Cat", image)
# cv.waitKey(0)

# Reading and showing video
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
