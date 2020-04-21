import cv2
import numpy as np
cap = cv2.VideoCapture('bird.avi');
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (596, 336))
ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while cap.isOpened():

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _,thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh, None, iterations=3)
    contour,_ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for i in contour:
        (x, y, w, h) = cv2.boundingRect(i)
        if cv2.contourArea(i) < 700:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 3)
    out.write(frame1)
    cv2.imshow("frame", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    key = cv2.waitKey(40)
    if key == 27 :
        break
cap.release()
out.release()
cv2.destroyAllWindows()