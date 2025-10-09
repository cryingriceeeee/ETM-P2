import cv2
import time

cap = cv2.VideoCapture(0)

frame_count = 0
start_time = time.time()
display_fps = 0  # value shown on screen

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    width = int(cap.get(3)) 
    height = int(cap.get(4))

    frame_count += 1
    current_time = time.time()

    if current_time - start_time >= 0.1:
        display_fps = frame_count / (current_time - start_time)
        frame_count = 0
        start_time = current_time

    # maybe use cv2.CAP_PROP_FPS?

    cv2.putText(frame, f"{int(display_fps)}", (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
