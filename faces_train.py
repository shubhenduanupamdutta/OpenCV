import os
import cv2 as cv
import numpy as np

people = [folder for folder in os.listdir("./Resources/Faces/train")]
DIR = "./Resources/Faces/train"

haar_cascade = cv.CascadeClassifier("./haar_face_default.xml")

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for image in os.listdir(path):
            image_path = os.path.join(path, image)
            image_array = cv.imread(image_path)
            gray = cv.cvtColor(image_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces_rect:
                # Region of interest (roi)
                faces_roi = gray[y: y+h, x: x+w]
                features.append(faces_roi)  # type: ignore
                labels.append(label)  # type: ignore


create_train()
print("Training done -----------------------------")

features = np.array(features, dtype="object")
labels = np.array(labels)

# Create Face Recognizer class
face_recognizer = cv.face.LBPHFaceRecognizer.create()

# train face recognizer on training data
face_recognizer.train(features, labels)  # type: ignore
face_recognizer.save("face_recognizer_trained.yaml")

np.save("features.npy", features)
np.save("labels.npy", labels)
