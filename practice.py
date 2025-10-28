import numpy as np
import cv2

img = cv2.imread('chessboard.png')
img = cv2.resize(img, (0,0), fx = 0.5, fy=0.5)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

alpha = 2
beta = -250
img = cv2.convertScaleAbs(img, alpha=alpha,beta=beta)

corners = cv2.goodFeaturesToTrack(grey, 100, 0.1, 10)
corners = np.intp(corners)

for corner in corners:
    corner = corner[0]
    x,y = corner.ravel()
    cv2.circle(img, (x,y), 3, (255, 0, 0), -1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

