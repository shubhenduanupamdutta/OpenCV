import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("blank", blank)

# image = cv.imread("./Resources/Photos/cat.jpg")
# cv.imshow("Cat", image)

# 1. Paint the color  a certain color
blank[:] = 0, 0, 255
# cv.imshow("Red", blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv.rectangle(blank, (250, 0), (500, 250), (0, 126, 126), thickness=cv.FILLED)
cv.rectangle(blank, (250, 250), (500, 500), (255, 0, 0), thickness=-1)

# 3. Draw a circle
cv.circle(blank, (250, 250), 100, (126, 126, 126), thickness=-1)

# 4. Draw a line
cv.line(blank, (100, 100), (400, 400), (0, 0, 0), thickness=3)

# 5. Write a text on the image
cv.putText(blank, "Shubhendu", (100, 250), fontFace=cv.FONT_HERSHEY_TRIPLEX,
           fontScale=1.4, color=(90, 90, 90), thickness=2)

cv.imshow("Rect", blank)


cv.waitKey(0)
