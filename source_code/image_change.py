import cv2
import os
from image_effect import *

path = '/home/ubuntu/test/dogs/dogs_3.jpg'

if os.path.isfile(path): # path의 경로에 존재하는지 확인
    img = cv2.imread(path)
else:
    print("not found")


actResize = 0
actRotate = 1
actBlur = 1
actCrop = 1

src = img


effect = imageEffect()


if actResize:
    src = effect.Resize(src)

if actRotate:
    src = effect.Rotate(src)

if actBlur:
    src = effect.Blur(src)

if actCrop:
    src = effect.Crop(src)


cv2.imshow("dogs",src)
cv2.waitKey()
cv2.destroyAllWindows()
