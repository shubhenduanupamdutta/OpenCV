import cv2 as cv

image = cv.imread("./Resources/Photos/group 1.jpg")
# cv.imshow("Original Image", image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Person", gray)

# Reading haar classifier
# Haar face classifier is very sensitive to noise, so it overestimates.
# One way to reduce noise sensitivity is
# By changing scaleFactor and minNeighbors
haar_cascade = cv.CascadeClassifier("./haar_face_default.xml")

# Detect face using above defined haar_cascade
faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=1)
# faces_rect will contain rectangular coordinates of faces as a list
print("Number of faces found", len(faces_rect))

# Drawing a rectangle over face(s) present
for (x, y, w, h) in faces_rect:
    # drawing rectangle
    cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)

cv.imshow("Detected Faces", image)

cv.waitKey(0)
