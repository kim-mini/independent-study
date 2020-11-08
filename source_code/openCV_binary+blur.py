import cv2
import os

path = "./source/data/lena.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
    src2 = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

resize = cv2.resize(src, dsize = (200, 200), interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
ret2, dst2 = cv2.threshold(gray, 100, 255, cv2.THRESH_TRIANGLE)
dst3 = cv2.blur(dst2, (2, 2), anchor = (-1, -1), borderType=cv2.BORDER_DEFAULT)


cv2.imshow("src", resize)
cv2.imshow("binary", dst)
cv2.imshow("binary2", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()