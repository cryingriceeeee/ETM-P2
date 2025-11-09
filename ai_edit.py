#EDIT BY DEEPSEEK

import cv2
import numpy as np
import simplejson as json
import random

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)

with open("colors.json", "r") as file:
    data = json.load(file)

colors = data["colors"]
length = len(colors)

def suisei_wa(r, g, b):
    """
    Find the closest matching color from the colors list
    """
    min_distance = float('inf')
    matched_color_index = 0
    
    for n in range(length):
        color = colors[n]
        rgb = np.array(color['rgb_array'])
        
        # Calculate Euclidean distance between colors
        distance = np.sqrt((r - rgb[0])**2 + (g - rgb[1])**2 + (b - rgb[2])**2)
        
        if distance < min_distance:
            min_distance = distance
            matched_color_index = n
            
    return matched_color_index

def kyou_mo_kawaii(color_index):
    """
    Get a random matching color from the combinations list
    """
    combinations = colors[color_index]['combinations']
    
    if combinations:  # Check if combinations list is not empty
        matching_color_index = random.choice(combinations)
        
        # Ensure the index is valid
        if matching_color_index < length:
            return matching_color_index
    
    # Return a default color if no valid combinations
    return color_index

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    height, width, _ = frame.shape
    cx = int(width / 2)

    # Sample colors from two points in the frame
    upper_frame = frame[50, cx]
    lower_frame = frame[350, cx]

    # Convert BGR to RGB
    ur, ug, ub = int(upper_frame[2]), int(upper_frame[1]), int(upper_frame[0])
    lr, lg, lb = int(lower_frame[2]), int(lower_frame[1]), int(lower_frame[0])
    
    upper_rgb = f"R: {ur} G: {ug} B: {ub}"
    lower_rgb = f"R: {lr} G: {lg} B: {lb}"

    # Draw markers and background rectangles
    cv2.circle(frame, (cx, 50), 5, (255, 225, 225), 3)
    cv2.circle(frame, (cx, 350), 5, (255, 225, 225), 3)
    cv2.rectangle(frame, (0, 30), (230, 60), (255, 255, 255), -1)
    cv2.rectangle(frame, (0, 330), (230, 360), (255, 255, 255), -1)
    cv2.rectangle(frame, (width - 250, 30), (width, 60), (255, 255, 255), -1)
    cv2.rectangle(frame, (width - 250, 330), (width, 360), (255, 255, 255), -1)

    # Find matching colors
    upper_color_idx = suisei_wa(ur, ug, ub)
    lower_color_idx = suisei_wa(lr, lg, lb)
    
    upper_color = colors[upper_color_idx]
    lower_color = colors[lower_color_idx]
    
    umc = colors[kyou_mo_kawaii(upper_color_idx)]
    lmc = colors[kyou_mo_kawaii(lower_color_idx)]

    # Extract RGB values for display
    upper_color_b, upper_color_g, upper_color_r = upper_color['rgb_array']
    lower_color_b, lower_color_g, lower_color_r = lower_color['rgb_array']
    umcb, umcg, umcr = umc['rgb_array']
    lmcb, lmcg, lmcr = lmc['rgb_array']

    # Convert to BGR for OpenCV
    upper_color_bgr = (upper_color_b, upper_color_g, upper_color_r)
    lower_color_bgr = (lower_color_b, lower_color_g, lower_color_r)
    umc_bgr = (umcb, umcg, umcr)
    lmc_bgr = (lmcb, lmcg, lmcr)

    # Display color names
    cv2.putText(frame, upper_color['name'], (10, 50), 0, 0.5, upper_color_bgr, 2)
    cv2.putText(frame, lower_color['name'], (10, 350), 0, 0.5, lower_color_bgr, 2)
    cv2.putText(frame, umc['name'], (width - 240, 50), 0, 0.5, umc_bgr, 2)
    cv2.putText(frame, lmc['name'], (width - 240, 350), 0, 0.5, lmc_bgr, 2)

    cv2.imshow('Color Recognizer', frame)
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()