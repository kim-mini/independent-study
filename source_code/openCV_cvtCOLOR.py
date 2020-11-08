import cv2
import os

path = "./source/data/lena.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
    src2 = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

#색공간바꾸기
dst1 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
dst2 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow("grayscale", dst1)
cv2.imshow("hsv", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()