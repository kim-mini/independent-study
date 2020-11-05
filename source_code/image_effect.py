import cv2
import numpy as np
from matplotlib import pyplot as plt


class imageEffect():

    def Resize(self, img):  # 이미지 리사이즈
        src = img
        size = (256, 256)
        dst = cv2.resize(src, dsize=size, interpolation=cv2.INTER_AREA)
        return dst

    def Rotate(self, img):  # 이미지 로테이션
        height, width, channel = img.shape
        matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
        dst = cv2.warpAffine(img, matrix, (width, height))
        return dst

    def Blur(self, img):  # 이미지 블러
        src = img
        blur = cv2.GaussianBlur(src, (5, 5), 0)
        return blur

    def Crop(self, img):  # 이미지크롭
        src = img
        dst = src.copy()
        dst = src[50:130, 100:180]
        return dst