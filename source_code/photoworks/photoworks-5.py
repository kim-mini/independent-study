import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import cv2
import numpy as np

import os


form_class = uic.loadUiType("photoworks.ui")[0]
# 이미지 경로 지정


class photoWorks(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.shar_1 = True
        self.image = np.ones((2,2))
        self.image2= self.image
        self.SaveImg = self.image2

        self.basic=1
        self.basic2=7
        self.imgSize1 = 120
        self.imgSize2 = 300

        self.basic_tab.setEnabled(False)
        self.effect_tab.setEnabled(False)
        self.mosaicVal.setEnabled(False)
        self.undoImglist = [self.image,]
        self.cnt = 0
        self.N = 128

        self.basicText.setText(str(self.basicVal.value()))

    def initUI(self):

        # open버튼을 눌렀을 때
        self.open_btn.clicked.connect(self.openFile)
        # save 버튼을 눌렀을 때
        self.save_btn.clicked.connect(self.saveFile)
        # blur 버튼을 눌렀을 때
        self.blur_btn.clicked.connect(self.AfterEffect)
        # sharpen 버튼을 눌렀을 때
        self.sharpen_btn.clicked.connect(self.AfterEffect)
        # none_btn 버튼을 눌렀을 때
        self.none_btn.clicked.connect(self.AfterEffect)
        self.invertCK.clicked.connect(self.AfterEffect)
        # press resetAll
        self.resetAll.clicked.connect(self.AllReset)
        # reset 버튼을 눌렀을 때
        self.resetbtn.clicked.connect(self.BasicReset)
        # press view_btn
        self.view_btn.clicked.connect(self.openViwer)
        # press undo_btn
        self.undo_btn.clicked.connect(self.UndoBnt)
        # grayscaleCK
        self.grayscaleCK.clicked.connect(self.AfterEffect)
        # press +
        self.p_btn.clicked.connect(self.window1Pbtn)
        # press -
        self.m_btn.clicked.connect(self.window1Mbtn)
        # crop
        self.cropCK.clicked.connect(self.ImgCrop)
        # mosaic
        self.mosaicCK.clicked.connect(self.AfterEffect)
        # mosaic value
        self.mosaicVal.setRange(0, 4)
        self.mosaicVal.setSingleStep(1)
        self.mosaicVal.setTickPosition(2)
        self.mosaicVal.valueChanged.connect(self.mosaicslider)



        # basic effect slider
        self.basicVal.setRange(0, 5)# slider값은 최대 5
        self.basicVal.setSingleStep(1)# 1칸당 1씩올라가게
        self.basicVal.setTickPosition(2)
        # 슬라이더 값이 바뀌었을 때
        self.basicVal.valueChanged.connect(self.basicslider)
        # 텍스트를 입력하고 엔터를 눌렀을 때
        self.basicText.returnPressed.connect(self.textChanged)

        # window1 scale slider
        self.window1S.setRange(0, 500)  # slider값은 최대 500
        self.window1S.setSingleStep(50)  # 1칸당 50씩올라가게
        self.window1S.setTickPosition(2)
        self.window1S.valueChanged.connect(self.window1Size)
        # window2 scale slider
        self.window2S.setRange(0, 500)  # slider값은 최대 1
        self.window2S.setSingleStep(50)  # 1칸당 1씩올라가게
        self.window2S.setTickPosition(2)
        self.window2S.valueChanged.connect(self.window2Size)






    def openFile(self):
        self.effect_tab.setEnabled(True)
        self.FileOpen,_ = QFileDialog.getOpenFileName(self, 'Open file', './')
        print("fname : {}".format(self.FileOpen), type(self.FileOpen))
        #print(len(self.FileOpen)) press cancel = return 0
        if len(self.FileOpen) == 0:
            self.image2
        # FileOpen : /home/ubuntu/PycharmProjects/pyqt5/photoworks/img/christoper.jpg <class 'str'>

        if not(len(self.FileOpen) == 0):

            self.image = cv2.imread(self.FileOpen)  # image read
            colCN = cv2.split(self.image)  # color = 3, gray =
            if len(colCN) == 3:
                self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)

            if len(colCN) == 1:
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

            self.image2 = self.image
            self.SaveImg = self.image
        self.window1S.setValue(0)
        self.window2S.setValue(0)
        # window 1
        self.importorg(self.image)
        # window 2
        self.importImg(self.image)

    def importorg(self,img):

        height, width = img.shape[:2]
        colCN = cv2.split(img)  # color = 3, gray = 1

        if len(colCN) == 3:
            convert = QImage(img.data, width, height, (img.nbytes / height),
                                  QImage.Format_RGB888)  # 이미지의 모든바이트, 넓이,길이,한라인의 바이트 수, 이미지 포맷
        elif len(colCN) == 1:
            convert = QImage(img.data, width, height, (img.nbytes / height),
                                  QImage.Format_Grayscale8)  # 이미지의 모든바이트, 넓이,길이,한라인의 바이트 수, 이미지 포맷

        scene1 = QGraphicsScene()  # gui에 표출
        tempmap1 = QPixmap.fromImage(convert)
        scene1.addPixmap(tempmap1.scaledToHeight(self.imgSize1))
        self.Window1.setScene(scene1)

    def importImg(self,img):  # 이미지 로드
        height, width = img.shape[:2]
        colCN = cv2.split(img) #color = 3, gray = 1

        if len(colCN) == 3:
            self.convert = QImage(img.data,width, height,(img.nbytes/height), QImage.Format_RGB888)#이미지의 모든바이트, 넓이,길이,한라인의 바이트 수, 이미지 포맷
        elif len(colCN) == 1:
            self.convert = QImage(img.data,width, height,(img.nbytes/height), QImage.Format_Grayscale8)#이미지의 모든바이트, 넓이,길이,한라인의 바이트 수, 이미지 포맷

        self.scene2 = QGraphicsScene()
        tempmap2 = QPixmap.fromImage(self.convert)
        self.scene2.addPixmap(tempmap2.scaledToHeight(self.imgSize2))
        self.Window2.setScene(self.scene2)

    def saveFile(self,dustImg):
        FileSave,_ = QFileDialog.getSaveFileName(self, 'Save file', './')
        print(FileSave)
        cv2.imwrite('{}'.format(FileSave),self.SaveImg)

    def AfterEffect(self):

        if self.blur_btn.isChecked():
            self.basic_tab.setEnabled(True)
            self.ImgBlur()


        if self.sharpen_btn.isChecked():
            if self.shar_1:
                self.basicVal.setValue(2)
                self.shar_1 = False
            self.basic_tab.setEnabled(True)
            self.ImgShar()

        if self.none_btn.isChecked():
            self.basic_tab.setEnabled(False)


        dstImg = self.image2

        if self.invertCK.isChecked():
            srcImg = dstImg
            dstImg = self.Imginvert(srcImg)

        if self.mosaicCK.isChecked():
            srcImg = dstImg
            dstImg = self.ImgMosaic(srcImg)

        if self.grayscaleCK.isChecked():
            srcImg = dstImg
            dstImg = self.ImgGrayscale(srcImg)

            self.importImg(dstImg)



        self.SaveImg = dstImg
        self.undoImglist.append(dstImg)
        self.cnt += 1
        self.importImg(dstImg)
        self.importorg(self.image)





    def ImgBlur(self):
        self.image2 = cv2.GaussianBlur(self.image, (self.basic, self.basic), 0)

    def ImgShar(self):
        kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, self.basic2, -1], [-1, -1, -1]])
        self.image2 = cv2.filter2D(self.image,-1,kernel_sharpen_1)

    def Imginvert(self,srcImg):
        dstImg = cv2.bitwise_not(srcImg)
        return dstImg

    def ImgGrayscale(self,srcImg):
        dstImg = cv2.cvtColor(srcImg,cv2.COLOR_BGR2GRAY)
        return dstImg

    def ImgCrop(self):
        roi = cv2.selectROI(self.image2)
        srcImg = self.image2

        dstImg = srcImg[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]
        colCN = cv2.split(srcImg)  # color = 3, gray = 1

        if len(colCN) == 3:
            dstImg = cv2.cvtColor(dstImg, cv2.COLOR_BGR2RGB)

        if len(colCN) == 1:
            dstImg = cv2.cvtColor(dstImg, cv2.COLOR_BGR2GRAY)

        #cv2.imshow('Img', dstImg)
        cv2.waitKey()
        cv2.destroyAllWindows()
        self.image2 = dstImg
        self.AfterEffect()

    def ImgMosaic(self,srcImg):
        self.mosaicVal.setEnabled(True)
        dstImg = np.zeros(srcImg.shape, dtype=srcImg.dtype)
        #print(dstImg)

        if len(srcImg.shape) == 1:
            height, width = srcImg.shape

        if len(srcImg.shape) == 3:
            height, width,_ = srcImg.shape

        h = height // self.N
        w = width // self.N

        for i in range(self.N):
             for j in range(self.N):
                 y = i*h
                 x = j*w
                 roi = srcImg[y:y+h, x:x+w]
                 if len(srcImg.shape) == 1:
                    dstImg[y:y+h, x:x+w] = cv2.mean(roi)[0]   # 그레이스케일 영상
                 if len(srcImg.shape) == 3:
                    dstImg[y:y+h, x:x+w] = cv2.mean(roi)[0:3] # 컬러영상

        return dstImg

    def window1Size(self):
        self.imgSize1 = self.window1S.value()+120
        self.AfterEffect()

    def window2Size(self):
        self.imgSize2 =  self.window2S.value()+300
        self.AfterEffect()

    def window1Pbtn(self):
        self.window1S.setValue(self.window1S.value()+50)

    def window1Mbtn(self):
        self.window1S.setValue(self.window1S.value()-50)

    def BasicReset(self):
        self.basicVal.setValue(0)
        self.AfterEffect()

    def AllReset(self):
        self.BasicReset()
        if self.invertCK.isChecked():
            self.invertCK.toggle()
        if self.grayscaleCK.isChecked():
            self.grayscaleCK.toggle()
        if self.mosaicidx.isChecked():
            self.mosaicidx.toggle()
        self.AfterEffect()

    def basicslider(self):
        # slider 값을 lineEdit에 보냄
        self.basicText.setText(str(self.basicVal.value()))
        if self.blur_btn.isChecked():
            self.basic2=7
            self.basic = self.basicVal.value() * 4 + 1
            self.basicVal.valueChanged.connect(self.AfterEffect)
        if self.sharpen_btn.isChecked():
            self.basic=1
            self.basic2 = self.basicVal.value() + 7
            self.basicVal.valueChanged.connect(self.AfterEffect)

    def mosaicslider(self):
        if self.mosaicCK.isChecked():
            mosaicidx = self.mosaicVal.value()
            mosaiclist = [128, 64, 32, 8, 4]
            self.N = mosaiclist[mosaicidx]
            self.mosaicVal.valueChanged.connect(self.AfterEffect)
        else:
            self.mosaicVal.setEnabled(False)
            
    def textChanged(self):
        # LenText에 있는 텍스트를 가져오는 메서드
        # object type = str
        targetSTR = self.basicText.text()
        self.basic_V = int(targetSTR)
        self.basicVal.setValue(self.basic_V)

    def openViwer(self):
        pass

    def UndoBnt(self):
        #print(self.undoImglist)
        dstImg = self.undoImglist[self.cnt]
        self.importImg(dstImg)
        self.cnt -= 1
        #self.undoImglist = self.undoImglist[:self.cnt]







if __name__ == "__main__" :

    app = QApplication(sys.argv)
    myWindow = photoWorks()
    myWindow.show()
    app.exec_()