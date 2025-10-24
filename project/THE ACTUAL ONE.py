import cv2
import numpy as np

def get_limits(color, tol=10):
    c = np.uint8([[color]])  
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = hsvC[0][0][0]

    min_saturation = 40  
    min_value = 40        

    if hue >= 165:
        lowerLimit = np.array([hue, min_saturation, min_value], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:
        lowerLimit = np.array([0, min_saturation, min_value], dtype=np.uint8)
        upperLimit = np.array([hue, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue, min_saturation, min_value], dtype=np.uint8)
        upperLimit = np.array([hue, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

orange = [0, 165, 255]

cap = cv2.VideoCapture(0)
while True: 
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=orange)

    mask = cv2.inRange(hsv, lowerLimit, upperLimit)

    cv2.imshow('frame', mask)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()