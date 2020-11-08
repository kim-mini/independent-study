import cv2
import os

path = "./source/data/lena.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(src, 100, 255)
sobel = cv2.Sobel(gray, cv2.CV_8U,1,0,3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U,ksize=3)
cv2.imshow("canny", canny)
cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)

cv2.waitKey(0)
cv2.destroyWindow()