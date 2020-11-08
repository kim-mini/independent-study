import cv2
import os

path = "./source/data/lena.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

dst = cv2.resize(src, dsize=(100, 100), interpolation = cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(0,0), fx = 0.5, fy =0.5, interpolation = cv2.INTER_AREA)

cv2.imshow("100x100", dst)
cv2.imshow("x:y", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()