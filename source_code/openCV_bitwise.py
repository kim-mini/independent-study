import cv2
import os

path = "./source/data/lena.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
    src2 = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

#이미지 비트연산
dst1 = cv2.bitwise_or(src, src2)
dst2 = cv2.bitwise_not(src)

cv2.imshow("xor", dst1)
cv2.imshow("not", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()