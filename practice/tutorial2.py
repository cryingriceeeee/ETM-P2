import numpy as np
import cv2

cap = cv2.VideoCapture(0) # takes input from webcam

while True:
        ret, frame = cap.read() # frame = image as numpy array, ret = tells u if it works
        width = int(cap.get(3)) # gets the width of the frame
        height = int(cap.get(4)) # gets the height of the frame


        image = np.zeros(frame.shape, np.uint8) # creates a black image of same size as frame
        smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) # resizes the frame to half its size   
        smaller_frame = cv2.rotate(smaller_frame, cv2.ROTATE_180) # rotates the smaller frame by 180 degrees
        image[:height//2, :width//2] = smaller_frame # places the smaller frame in the top-left corner of the black image
        image[height//2:, :width//2] = smaller_frame # places the smaller frame in the bottom-left corner 
        image[:height//2, width//2:] = smaller_frame # places the smaller frame in the top-right corner 
        image[height//2:, width//2:] = smaller_frame # places the smaller frame in the bottom-right corner 
        




        cv2.imshow('frame', image) # shows the image in a window named 'frame'
        if cv2.waitKey(100) == ord('q'): # waits for 100ms, if 'q' is pressed, break the loop
                break


cap.release() # releases the webcam
cv2.destroyAllWindows() # closes all the windows opened by opencv