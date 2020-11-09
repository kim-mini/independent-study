from OpenCV_Python.img.calibration import *
import os
import cv2

path = "/home/ubuntu/PycharmProjects/opencv/OpenCV_Python/img/note2"

filelist = os.listdir(path)
#cv2.imshow('img', img)
mtx,dist = calib()

for filename in filelist:
    newpath = os.path.join(path,filename)
    img = cv2.imread(newpath)

    undist_img = undistort(img, mtx, dist)
    cv2.imshow('before', img)
    cv2.imshow('undist_img', undist_img)
    cv2.waitKey()
    cv2.destroyAllWindows()


