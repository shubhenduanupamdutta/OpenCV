import cv2 as cv
import numpy as np

image = cv.imread("./Resources/Photos/park.jpg")
cv.imshow("Original Park Image", image)


# Translations
def translation(img, x: int, y: int):
    """
    Returns a translated image by x and y
    +x and +y value means shifting Right and Down while
    -x and -y value means shifting Left and Up

    Args:
        img (MatLike): Image object obtained after reading image file using
        imread()
        x (int): Translations in x direction
        y (int): Translations in y direction

    Returns:
        image: Translated image using warpAffine

    """
    transMat = np.array([[1, 0, x], [0, 1, y]], dtype=np.float32)
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translation(image, 100, 100)
# cv.imshow("Translated image", translated)


# Rotating the image
def rotate(img, angle: float, rotation_point: tuple[int, int] | None = None):
    """
    Returns a rotated image when image, angle and rotation point is provided.
    +ve angle means anti-clockwise rotation
    -ve angle means clockwise rotation

    Args:
        img (MatLike): Image object obtained after reading an image
        using cv.imread()
        angle (float): Angle in degrees
        rotation_point (tuple[int, int] | None, optional): The point by which
        to rotate in essence center of rotation. Defaults to None.

    Returns:
        img (MatLike): Rotated image

    """
    height, width = img.shape[:2]
    if not rotation_point:
        rotation_point = (width // 2, height // 2)
    rotMatrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMatrix, dimensions)


rotated = rotate(image, 45)
# cv.imshow("Rotated Image", rotated)


# Flipping the image
# 2nd argument is flipCode:
# 0 means Vertical (axis of rotation x-axis)
# 1 means Horizontal (axis of rotation y-axis)
# -1 means both Horizontal and Vertical

flipped = cv.flip(image, -1)
cv.imshow("Flipped Image", flipped)

cv.waitKey(0)
