import cv2
import numpy as np
import simplejson as json

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)

while True:
    _, frame = cap.read()
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)
    cyhalf = int(cy/2)

    upper_frame = frame[cy - cyhalf,cx]
    lower_frame = frame[cy + cyhalf,cx]

    print(upper_frame)
    print(lower_frame)

    ur, ug, ub = int(upper_frame[2]), int(upper_frame[1]), int(upper_frame[0])
    lr, lg, lb = int(lower_frame[2]), int(lower_frame[1]), int(lower_frame[0])
    upper_rgb = "R: " + str(ur) + " G: " + str(ug) + " B: " + str(ub)
    lower_rgb = "R: " + str(lr) + " G: " + str(lg) + " B: " + str(lb)

    # with open('original_colors.json', 'r') as file:
    #     data = json.load(file)
    # for color in data:
    #     rgb = color['rgb_array']
    #     placeholder_r = 0
    #     placeholder_g = 0
    #     placeholder_b = 0
    #     if abs(r - rgb[0]) < abs(placeholder_r - rgb[0]) and abs(g - rgb[1]) < abs(placeholder_g - rgb[1]) and abs(b - rgb[2]) < abs(placeholder_b - rgb[2]):
    #         placeholder_r = abs(r - rgb[0])
    #         placeholder_g = abs(g - rgb[1])
    #         placeholder_b = abs(b - rgb[2])
    #         matched_color = color['name']

    cv2.circle(frame, (cx,cy + cyhalf), 5, (255,225,225), 3)
    cv2.circle(frame, (cx,cy - cyhalf), 5, (255,225,225), 3)
    cv2.putText(frame, upper_rgb, (10,50), 0, 1, (ub,ug,ur), 2)
    cv2.putText(frame, lower_rgb, (10,350), 0, 1, (lb,lg,lr), 2)
    # cv2.putText(frame, matched_color, (10,100), 0, 1, (b,g,r), 2)

    cv2.imshow('Color Recognizer', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()