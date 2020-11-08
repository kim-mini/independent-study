import cv2
import os

path = "./source/data/lena.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
    src2 = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

#이미지 크롭하기
dst = src.copy()
dst = src[100:400, 200:700]


cv2.imshow("crop", dst)

cv2.waitKey(0)
cv2.destroyWindow(dst)