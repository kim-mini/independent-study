import cv2
import os

path = "./source/data/lena.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

height, width, channel = src.shape
imgAxis =(height/2, width/2)

metrix = cv2.getRotationMatrix2D(imgAxis, 90, 1)
dst = cv2.warpAffine(src, metrix,(height, width))

cv2.imshow("Rotate", dst)
cv2.waitKey(0)
cv2.destroyWindow(dst)