#0311.py
import numpy as np
import cv2


def posxy(a, b):
    if a < b:
        return a
    else:
        return b

def onMouse(event, x, y, flags, param):
    global img
    global pt1
    if event == cv2.EVENT_LBUTTONDOWN: # 클릭했을 때의 x, y 값
        pt1 = x,y
    elif event == cv2.EVENT_LBUTTONUP: # 마우스클릭을 끝냈을 때의 x, y 값
        pt2 = x,y
        cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2) # 사각형 그려진

        a = (pt2[0] - pt1[0]) # 사각형을 밑에서 위로 올려도 길이를 구할 수 있도록
        b = (pt2[1] - pt1[1])

        if a < 0:
            a = a*-1

        if b < 0:
            b = b*-1

        text = '{} x {}'.format(a, b) # txt 출력 할 문구

        txtX = posxy(pt1[0], pt2[0])
        txtY = posxy(pt1[1], pt2[1])
        org = txtX+5,txtY+15 # txt의 위치
        font = cv2.FONT_HERSHEY_SIMPLEX #font character

        cv2.putText(img, text, org, font, 0.5, (255, 0, 0), 2) #txt info

    elif event == cv2.EVENT_LBUTTONDBLCLK:
        img = np.zeros((512, 512, 3), np.unit8) + 255
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param[0], (x, y), 5, (0, 0, 255), 3)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        param[0] = np.zeros(param[0].shape, np.uint8) + 255   
    cv2.imshow("img", param[0])
    
img = np.zeros((512,512,3), np.uint8) + 255
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse, [img])
cv2.waitKey()
cv2.destroyAllWindows()
