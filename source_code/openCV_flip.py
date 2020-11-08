import cv2
import os

path = "./source/data/lena.jpg"
if os.path.isfile(path):
    src = cv2.imread(path)
else :
    print("not found this path : '{}'".format(path))

dsc = cv2.flip(src, 0)
dsc2 = cv2.flip(src, 1)

cv2.imshow("flip 0", dsc)
cv2.imshow("flip 1", dsc2)
cv2.waitKey()
cv2.destroyAllWindows()