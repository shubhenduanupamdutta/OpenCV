import cv2 as cv
import numpy as np

image = cv.imread("./Resources/Photos/cats.jpg")
cv.imshow("Original Cat Image", image)

# Creating a blank image
blank = np.zeros(image.shape, dtype=np.uint8)


gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
# cv.imshow("Grayed", gray)

# *********************************************************
# First method, blur the image and then detect using canny
# *********************************************************
# # Blur the image to get a better contour
# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blurred Image", blur)

# # Detecting edges
# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny", canny)
# *********************END First Method*****************************

# **************************************************
# Second Method Using Thresholds
# **************************************************
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)


# Finding contours
# findContours method returns contours and hierarchies
# Takes edges (here canny) and modes to find contours
# RETR_TREE -> All Hierarchial contours
# RETR_EXTERNAL -> External Contours
# RETR_LIST -> All Contours
# CHAIN_APPROX_NONE -> Approximate method, no approximation
# CHAIN_APPROX_SIMPLE -> compresses result
contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST,
                                      cv.CHAIN_APPROX_SIMPLE)
print(f"There are {len(contours)} contours in the image.")

# Drawing contours on the blank image
cv.drawContours(blank, contours, -1, (0, 0, 255), thickness=2)
cv.imshow("Contours", blank)

cv.drawContours(image, contours, -1, (255, 0, 0), thickness=1)
cv.imshow("Image with Contours", image)

cv.waitKey(0)
