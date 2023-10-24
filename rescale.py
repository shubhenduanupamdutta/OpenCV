"""
Rescaling and Resizing images and videos in OpenCV
"""

import cv2 as cv

# image = cv.imread("./Resources/Photos/cat_large.jpg")
# cv.imshow("Cat", image)


def rescale(frame, scale: float = 0.75):
    """
    rescales frame (usually a cv2.typing.MatLike object) by scale

    Args:
        frame (_type_): frame containing the image or video
        scale (float, optional): Value by which to scale, Multiply the current
        values of width and height by. Defaults to 0.75.

    Returns:
        frame: resized frame using cv.resize
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_resolution(width: int, height: int):
    """
    Changes resolution for live streams i.e. directly from webcam or similar.

    Args:
        width (int): Width of the changed frame
        height (int): Height of the changed frame
    """
    capture.set(3, width)
    capture.set(4, height)  # 3 & 4 are correspondingly width and height


capture = cv.VideoCapture("./Resources/Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()
    resized_frame = rescale(frame, 0.2)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', resized_frame)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
