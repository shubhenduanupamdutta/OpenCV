import cv2 as cv

image = cv.imread("./Resources/Photos/park.jpg")
cv.imshow("Original", image)

# Converting the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
# cv.imshow("Grayscale", gray)

# Blur an image
blur = cv.GaussianBlur(image, (3, 3), cv.BORDER_DEFAULT)
# Kernel size (3, 3) here, can be increased to increase the blur
# cv.imshow("Blurred", blur)

# Edge Cascade
edge_cascade = cv.Canny(image, 125, 175)
# to reduce the amount of edges, we can blur the image first,
# in this case passing blur instead of image will reduce edges
# cv.imshow('EdgeCascade', edge_cascade)

# How to dilate image using structuring element
dilated = cv.dilate(edge_cascade, 
                    cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2)),
                    iterations=1)
# cv.imshow("Dilated", dilated)

eroded = cv.erode(dilated, cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2)),
                  iterations=1)
# cv.imshow("Eroded", eroded)

# Cropping image
cropped = image[0:250, 250: 500]
cv.imshow("Cropped", cropped)


cv.waitKey(0)
