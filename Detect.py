#!/usr/bin/python3

import cv2 as cv
import imutils
import threading
import play_sound

cap = cv.VideoCapture(0, cv.CAP_DSHOW)


cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)


_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv.cvtColor(start_frame, cv.COLOR_BGR2GRAY)
start_frame = cv.GaussianBlur(start_frame, (21, 21), 0)

alarm = False
alarm_mode = False
alarm_counter = 0

while True:

    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    if alarm_mode:
        frame_bw = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_bw = cv.GaussianBlur(frame_bw, (5, 5), 0)

        difference = cv.absdiff(frame_bw, start_)
        threshold = cv.threshold(difrence, 25, 255, cv.THRESH_BINARY)[1]
        start_frame = frame_bw

        if threshold.sum() > 3000:
            alarm_counter = 1
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
            
        cv.imshow("Cam", threshold)
    else:
        cv.imshow("Cam", frame)
    
    if alarm_counter > 20:
        if not alarm:
            alarm = True
            play_sound.play_beep()
        
        key_pressed = cv.waitKey(30)
        if key_pressed == ord("t"):
            alarm_mode = not alarm_mode
            alarm_counter = 0
        if key_pressed == ord("q"):
            alarm_mode = False
            break

cap.release()
cv.destroyAllWindows()
