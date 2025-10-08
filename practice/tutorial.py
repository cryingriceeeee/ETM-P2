import cv2 as cv
import numpy as np

img = cv.imread('mavs_logo.jpg', -1) # imread('folder name/mavs_logo.jpg', -1) 

# -1, cv.IMREAD_GRAYSCALE = load image in grayscale
# 0, cv.IMREAD_COLOR = load image in color
# 1, cv.IMREAD_UNCHANGED = load image without transparency

img = cv.resize(img, (0,0), fx=0.5, fy=0.5) # resize image by 50% in both dimensions
# cv.resize(img, (100, 100)) # resize image to 100x100 pixels

# img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE) rotate image 90 degrees clockwise

# instead of RGB (red, green, blue), OpenCV uses BGR (blue, green, red)
# print(img[x][y]) # prints the BGR values of the pixel at (x, y), can use (x:y) to get a range of pixels

# print(img.shape) # prints the dimensions of the image (height, width, channels)
# print(img.size) # prints the total number of pixels in the image (height * width * channels)

cv.imshow('image', img) # 'image' = window name
cv.waitKey(0) # 0 = wait indefinitely until a key is pressed, any other number = wait that many milliseconds
cv.destroyAllWindows() # close all windows
