import cv2
import os

path = "./source/data/lena.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

#hsv로 변환
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
h = cv2.inRange(h,5,20)
#mask씌우기
dst = cv2.bitwise_and(hsv,hsv, mask = h)
dst = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)

cv2.imshow("hsv", dst)
cv2.waitKey(0)
cv2.destroyWindow(dst)