import cv2
import numpy as np
import simplejson as json
import time
import random

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)

with open("colors.json", "r") as file:
    data = json.load(file)

colors = data["colors"]
length = len(colors)

last_update_time = 0
update_interval = 1  
upper_color = None
lower_color = None  

def suisei_wa(a, b, c):
    r, g, b, = a, b, c
    n = 0
    matched_color_index = 0
    placeholder_r = 0
    placeholder_g = 0
    placeholder_b = 0

    while n < length:
        color = colors[n]
        rgb = np.array(color['rgb_array'])

        if abs(r - rgb[0]) < abs(placeholder_r - rgb[0]) and abs(g - rgb[1]) < abs(placeholder_g - rgb[1]) and abs(b - rgb[2]) < abs(placeholder_b - rgb[2]):
            placeholder_r = abs(r - rgb[0])
            placeholder_g = abs(g - rgb[1])
            placeholder_b = abs(b - rgb[2])
            matched_color_index = n

        n += 1

    return matched_color_index

def kyou_mo_kawaii(a):
    combinations = colors[a]['combinations']
    
    if not combinations:
        return a
    
    for _ in range(10):
        matching_color_index = random.choice(combinations)
        if matching_color_index <= 157:
            return matching_color_index

    return a

while True:
    _, frame = cap.read()
    height, width, _ = frame.shape

    cx = int(width/2)

    upper_frame = frame[50,cx]
    lower_frame = frame[350,cx]

    ur, ug, ub = int(upper_frame[2]), int(upper_frame[1]), int(upper_frame[0])
    lr, lg, lb = int(lower_frame[2]), int(lower_frame[1]), int(lower_frame[0])
    upper_rgb = "R: " + str(ur) + " G: " + str(ug) + " B: " + str(ub)
    lower_rgb = "R: " + str(lr) + " G: " + str(lg) + " B: " + str(lb)

    cv2.circle(frame, (cx,50), 5, (255,225,225), 3)
    cv2.circle(frame, (cx,350), 5, (255,225,225), 3)
    cv2.rectangle(frame, (0,30), (230,60), (255,255,255), -1)
    cv2.rectangle(frame, (0,330), (230,360), (255,255,255), -1)
    cv2.rectangle(frame, ((width ),30), ((width - 250),60), (255,255,255), -1)
    cv2.rectangle(frame, ((width),330), ((width - 250),360), (255,255,255), -1)
    
    current_time = time.time()
    if current_time - last_update_time >= update_interval:
        upper_color = colors[suisei_wa(ur, ug, ub)]
        lower_color = colors[suisei_wa(lr, lg, lb)]
        umc = colors[kyou_mo_kawaii(suisei_wa(ur, ug, ub))]
        lmc = colors[kyou_mo_kawaii(suisei_wa(lr, lg, lb))]
        last_update_time = current_time
    
    # upper_color = colors[suisei_wa(ur, ug, ub)]
    # lower_color = colors[suisei_wa(lr, lg, lb)]
    # umc = colors[kyou_mo_kawaii(suisei_wa(ur, ug, ub))]
    # lmc = colors[kyou_mo_kawaii(suisei_wa(lr, lg, lb))]

    upper_color_b = upper_color['rgb_array'][2]
    upper_color_g = upper_color['rgb_array'][1]
    upper_color_r = upper_color['rgb_array'][0]

    lower_color_b = lower_color['rgb_array'][2]
    lower_color_g = lower_color['rgb_array'][1]
    lower_color_r = lower_color['rgb_array'][0]

    umcb = umc['rgb_array'][2]
    umcg = umc['rgb_array'][1]
    umcr = umc['rgb_array'][0]

    lmcb = lmc['rgb_array'][2]
    lmcg = lmc['rgb_array'][1]
    lmcr = lmc['rgb_array'][0]

    cv2.putText(frame, upper_color['name'], (10,50), 0, 0.5, (upper_color_b,upper_color_g,upper_color_r), 2)
    cv2.putText(frame, lower_color['name'], (10,350), 0, 0.5, (lower_color_b,lower_color_g,lower_color_r), 2)
    cv2.putText(frame, umc['name'], (cx + 70,50), 0, 0.5, (umcb,umcg,umcr), 2)
    cv2.putText(frame, lmc['name'], (cx + 70,350), 0, 0.5, (lmcb,lmcg,lmcr), 2)

    cv2.imshow('Color Recognizer', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()