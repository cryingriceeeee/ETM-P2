import numpy as np
import cv2

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


cap = cv2.VideoCapture(0) # takes input from webcam

while True: # infinite loop
        ret, frame = cap.read() # frame = returns image pixels as numpy array, ret = tells u if it works
        width = int(cap.get(3)) # gets the width of the frame
        height = int(cap.get(4)) # gets the height of the frame

        img  = cv2.line(frame, (0,0), (width//2,height//2), (255,0,0), 5) # draws a blue line from top-left to bottom-right
        img = cv2.rectangle(frame, (0,0), (width//2,height//2), (0,255,0), 5) # draws a green rectangle in the top-left corner
        font = cv2.FONT_HERSHEY_SIMPLEX # sets the font for the text
        img = cv2.putText(frame, str(cv2.CAP_PROP_FPS), (10,height-10), font, 1, (255,255,255), 1, cv2.LINE_AA)

        cv2.imshow('frame', frame) # shows the image in a window named 'frame'
        
        if cv2.waitKey(100) == ord('q'): # waits for 100ms, if 'q' is pressed, break the loop
                break

cap.release() # releases the webcam
cv2.destroyAllWindows() # closes all the windows opened by opencv