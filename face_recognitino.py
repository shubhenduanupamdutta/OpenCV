import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier("./haar_face_default.xml")
name = [folder_name for folder_name in os.listdir("./Resources/Faces/train")]

features = np.load("./features.npy", allow_pickle=True)
labels = np.load("./labels.npy", allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.read("./face_recognizer_trained.yaml")


# Validate model
# Read an image
image = cv.imread("./Resources/Faces/val/madonna/1.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Grayed Face", gray)

# Detect face in the image
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in face_rect:
    faces_roi = gray[y: y+h, x: x+h]

    labels, confidence = face_recognizer.predict(faces_roi)
    print(f"Labels = {name[labels]} with confidence = {confidence}")

    cv.putText(image, f"{name[labels]}", (20, 20), cv.FONT_HERSHEY_COMPLEX,
               0.6, (0, 255, 0), 2)
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Detected Face", image)

cv.waitKey(0)
