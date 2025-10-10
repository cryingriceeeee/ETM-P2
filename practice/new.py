import numpy as np
import cv2

from PIL import Image

from util import get_limits

# img = cv.imread(image, color value) -> reads an image from a file
        # image = path to image
        # color values:
                # -1 -> load image in grayscale
                # 0 -> load image in full color
                # 1 -> load image without transparency

# img = cv.resize(img, (0,0), fx=0.5, fy=0.5) -> resize image by 50% in both dimensions
# img = cv.resize(img, (100, 100)) -> resize image to 100x100 pixels

# instead of RGB (red, green, blue), OpenCV uses BGR (blue, green, red)

# cv.imshow(name, img) -> shows the image in a window named 'image'
        # name = name of the window

orange = [0,165,255]

cap = cv2.VideoCapture(0) # takes input from webcam

while True: # infinite loop
        ret, frame = cap.read() # frame = returns image pixels as numpy array, ret = tells u if it works
        width = int(cap.get(3)) # gets the width of the frame
        height = int(cap.get(4)) # gets the height of the frame

        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # converts the image from BGR to HSV
        lowerLimit, upperLimit = get_limits(orange) # gets the lower and upper limits for the color orange

        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) # creates a mask that only shows the color orange
        mask_ = Image.fromarray(mask) # converts the mask to a PIL image
        bbox = mask_.getbbox() # gets the bounding box of the mask

        if bbox: # if the bounding box is not None
                x1, y1, x2, y2 = bbox # unpacks the bounding box
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2) # draws a green rectangle around the object


        # img  = cv2.line(frame, (0,0), (width//2,height//2), (255,0,0), 5) # draws a blue line from top-left to bottom-right
        # img = cv2.rectangle(frame, (0,0), (width//2,height//2), (0,255,0), 5) # draws a green rectangle in the top-left corner



        cv2.imshow('frame', frame) # shows the image in a window named 'frame'
        
        if cv2.waitKey(100) == ord('q'): # waits for 100ms, if 'q' is pressed, break the loop
                break

cap.release() # releases the webcam
cv2.destroyAllWindows() # closes all the windows opened by opencv