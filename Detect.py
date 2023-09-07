#!/usr/bin/python3

import cv2 as cv
import imutils
import threading
import play_sound

cap = cv.VideoCapture(0)


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
        threshold = cv.