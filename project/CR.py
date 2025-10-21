import cv2 # imports opencv packages


cap = cv2.VideoCapture(0) # stores camera input as a variable
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # sets frame width to 1280 pixels
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 780) # sets frame height to 780 pixels

while True: # infinite loop
    _, frame = cap.read() # activates camera 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # converts frame to HSV color model

    height, width, _ = frame.shape # sets frame size

    cx = int(width / 2) # finds center x coordinates
    cy = int(height / 2) # finds center y coordinates
    
    cyhalf = cy / 2
    cyup = int(cy + cyhalf) 
    cydown = int(cy - cyhalf)


    up = frame[cx, cyup]
    down = frame[cx, cydown]

    uphue_value = up[0] 
    downhue_value = down[0] 


    upcolor = "Undefined" # initializes color variable
    if uphue_value < 5:
        upcolor = "Red"
    elif uphue_value < 22:
        upcolor = "Orange"
    elif uphue_value < 33:
        upcolor = "Yellow"
    elif uphue_value < 78:
        upcolor = "Green"
    elif uphue_value < 131:
        upcolor = "Blue"
    elif uphue_value < 170:
        upcolor = "Violet"
    else:
        upcolor = "Red"

    downcolor = "Undefined" # initializes color variable
    if downhue_value < 5:
        downcolor = "Red"
    elif downhue_value < 22:
        downcolor = "Orange"
    elif downhue_value < 33:
        downcolor = "Yellow"
    elif downhue_value < 78:
        downcolor = "Green"
    elif downhue_value < 131:
        downcolor = "Blue"
    elif downhue_value < 170:
        downcolor = "Violet"
    else:
        downcolor = "Red"

    print(up) 
    print(down) 
    cv2.putText(frame, upcolor, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2) 
    cv2.putText(frame, downcolor, (100,250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2) 
    cv2.circle(frame, (cx,cyup), 5, (255,255,255), 3) 
    cv2.circle(frame, (cx,cydown), 5, (255,255,255), 3) 

    cv2.imshow("Frame", frame) # diplsays camera input
    key = cv2.waitKey(1) # after "Esc" is pressed, then waits 1 millisecond before registering a response
    if key == 27: # if "Esc" is pressed, the loop stops
        break

cap.release() # deactivates camera
cv2.destroyAllWindows # closes all windows