import numpy as np
import cv2
import matplotlib.image as mpimg
import glob

# Read in and make a list of calibration images
images = glob.glob('/home/ubuntu/PycharmProjects/opencv/OpenCV_Python/img/sample2/chess_*.jpg')


# Array to store object points and image points from all the images

objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

def calib():
    #어느정도 반복을 할 지 정해주는 기준
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    # Prepare object points
    objp = np.zeros((9 * 7, 3), np.float32)
    
    #mgrid[]는 반대로 출력이 되기때문에 반대로 입력을 해주어야 한다 
    objp[:, :2] = np.mgrid[0:7, 0:9].T.reshape(-1, 2)  # x,y coordinates

    for fname in images:


        img = cv2.imread(fname)
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 체스판의 코너찾기
        ret, corners = cv2.findChessboardCorners(gray, (7, 9), None)

        # 찾았으면 objpoints, imgpoints에 추가하
        if ret == True:

            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            imgpoints.append(corners)

            img = cv2.drawChessboardCorners(img,(7,6),corners2,ret)
            cv2.imshow('img', img)
            cv2.waitKey()

        else:
            continue기

    cv2.destroyAllWindows()

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    return mtx, dist

def undistort(img, mtx, dist):
    """ undistort image """
    return cv2.undistort(img, mtx, dist, None, mtx)

