import numpy as np
import cv2
from matplotlib  import pyplot as plt
def nothing(x):
    pass


#cv2.namedWindow("tracking")


#cv2.createTrackbar("lh", "tracking", 0, 255, nothing)
#cv2.createTrackbar("ls", "tracking", 0, 255, nothing)
#cv2.createTrackbar("lv", "tracking", 0, 255, nothing)
#cv2.createTrackbar("uh", "tracking", 255, 255, nothing)

#cv2.createTrackbar("us", "tracking", 255, 255, nothing)
#cv2.createTrackbar("uv", "tracking", 255, 255, nothing)
#while True:
frame = cv2.imread("Piechart.png")
NEW = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #lh = cv2.getTrackbarPos("lh", "tracking")
    #ls = cv2.getTrackbarPos("ls", "tracking")
    #lv = cv2.getTrackbarPos("lv", "tracking")
    #uh = cv2.getTrackbarPos("uh", "tracking")
    #us = cv2.getTrackbarPos("us", "tracking")
    #uv = cv2.getTrackbarPos("uv", "tracking")

lb = np.array([20, 87, 214])
ub = np.array([33, 255, 255])
mask = cv2.inRange(hsv, lb, ub)

res = cv2.bitwise_and(frame, frame, mask=mask)
img = cv2.cvtColor(res ,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img,127,255,0)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(res,contours,-1,(0,255,0),5 )
RESULT = cv2.cvtColor(res,cv2.COLOR_BGR2RGB)
titles = ["original","yellow-slice"]
images = [NEW,RESULT]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i] ,)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
    #cv2.imshow("original", frame)
    #cv2.imshow("mask", mask)
    #cv2.imshow("yellow_slice", res)
    #key = cv2.waitKey(1)
    #if key == 27:
       # break
#cv2.destroyAllWindows()
