import os
import cv2

cnt = 0
path = "."
fileList = os.listdir(path)
ext = '.png'


for filename in fileList:
    if filename.endswith(ext):
        cnt += 1
        srcpath = os.path.join(path,filename)
        src = cv2.imread(srcpath)
        b, g, r = cv2.split(src)

        DustFilenameB = path+"/"+filename.split(".")[0]+"_B"+ext
        DustFilenameG = path + "/" + filename.split(".")[0] + "_G" + ext
        DustFilenameR = path + "/" + filename.split(".")[0] + "_R" + ext
        cv2.imwrite(DustFilenameR, r)
        cv2.imwrite(DustFilenameG, g)
        cv2.imwrite(DustFilenameB, b)
        # cv2.imshow("b",b)
        # cv2.imshow("G", g)
        # cv2.imshow("R", r)
        #print(DustFilenameB)

    else:
        print('no more')

# cv2.waitKey() #아무키나 입력받아도 된다
# cv2.destroyAllWindows()
print('is have {} file'.format(cnt))


