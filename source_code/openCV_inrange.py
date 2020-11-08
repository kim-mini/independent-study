import cv2
import os

path = "./source/data/SegmentTest.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

lower_red = cv2.inRange(hsv, (0, 100,100), (5,255,255))
upper_red = cv2.inRange(hsv, (170,100,100),(180,255,255))
added_red = cv2.addWeighted(lower_red,1.0,upper_red,1.0,0.0)

red = cv2.bitwise_and(hsv,hsv,mask=added_red)
red = cv2.cvtColor(red,cv2.COLOR_HSV2BGR)

cv2.imshow("red", red)
cv2.waitKey(0)
cv2.destroyAllWindows()