#!/usr/bin/env python3
import cv2
import time
import recognition

# The duration in seconds of the video captured


capture_duration = 3
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/opt/frtsys/outputvideo/output.avi',fourcc, 20.0, (640,480))

start_time = time.time()
while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame, 1)
        out.write(frame)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
