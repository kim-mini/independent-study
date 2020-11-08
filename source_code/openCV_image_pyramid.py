import cv2
import os

path = "./source/data/lena.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

height, width, channel = src.shape
dst1 = cv2.pyrUp(src)
dst2 = cv2.pyrDown(src)

cv2.imshow("x2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()