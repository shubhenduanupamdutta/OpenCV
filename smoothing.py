import cv2 as cv

image = cv.imread("./Resources/Photos/cats.jpg")
cv.imshow("Original Image", image)

# Kernel size, odd number tuples (n, n)
# Determines the value of middle pixel using nxn surrounding pixels
# Larger the kernel size, more the blur

# Blurring using averaging
average = cv.blur(image, (3, 3))
cv.imshow("Average", average)


# Gaussian Blur (more natural alternative, since weights been applied to each
# pixel value before calculating averages)
gaussian = cv.GaussianBlur(image, (3, 3), 0)  # third value is std. deviation
cv.imshow("Gaussian Blur", gaussian)

# Median blur - Basically same thing as averaging except for finding median
# instead of average. Median blur is more effective in reducing noise in the
# image than average or even gaussian blur.
# Note: Median blur is not for large kernel sizes
median = cv.medianBlur(image, 3)
cv.imshow("Median Blur", median)

# Bilateral Blurring
# It applies blurring but it retains the edges in the image
# 2nd argument is not kernel but diameter as int
# 3rd argument is sigmaColor - larger values means more colors to consider in
# neighborhood
# 4th argument is sigmaSpace - further out pixels effect calculates -> larger
# values means effect of distant pixels
bilateral = cv.bilateralFilter(image, 10, 35, 25)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)
