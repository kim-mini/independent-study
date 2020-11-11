import cv2
import os
import numpy as np
import sys


def notting(pos): # 트랙바 핸들러
    pass
def player(path, filename):
    file = os.path.join(path, filename)

    frameRate = 20
    swich = 0


    image = None
    flag = 0 #정지 상태
    L_TH = 0 #트랙바 low
    H_TH = 0 #트랙바 high


    cv2.namedWindow('video') # 창 생성
    cap = cv2.VideoCapture(file)
    #print(cap.get(cv2.CAP_PROP_FPS)) 프레임레이트확인 : 20

    # 트랙바 생성
    cv2.createTrackbar('Low_TH', 'video', 0, 255, notting) # video에는 트랙바를 생성 할 창이름을 적어주세요
    cv2.createTrackbar('High_TH', 'video', 0, 255, notting) # video에는 트랙바를 생성 할 창이름을 적어주세요


    while 1: # 비디오재생
        if flag == 1:# push - space bar
            frame = image
        else:
            ret, frame = cap.read()
            if not ret:# while문을 빠져나오기 위한 조건문
                break
        cv2.imshow('video',frame)
        # 63 52
        # target bar의 위치값을 받음
        Low_TH = cv2.getTrackbarPos('Low_TH', 'video')
        High_TH = cv2.getTrackbarPos('High_TH', 'video')

        key = cv2.waitKey(33)
        if key == 32: # space
            flag = not flag
            image = frame
        elif key == 112 :# p
            L_TH = Low_TH
            H_TH = High_TH
            print(L_TH, H_TH)
        elif key == 113: # q
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":#동영상 파일 경로
    path = "/home/ubuntu/PycharmProjects/laneDetect/miniproject/"
    filename = '2020111017.avi'
    player( path, filename )
