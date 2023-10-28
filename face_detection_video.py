import cv2 as cv

capture = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier("./haar_face_default.xml")

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow("Video", frame)

    key = cv.waitKey(20)
    if key == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
