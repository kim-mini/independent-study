import os
import shutil

path = 'C:/Users/82106/Desktop/아바텍 Report'
dirName = {1:'1.Top',2:'2.Front',3:'3.Bottom',4:'4.Rear',5:'5.T1',6:'6.T2'}

def fileList(dir_name : str)->list :
    file_list = os.listdir(dir_name)
    for file in file_list:
        srcPath = os.path.join(dir_name,file)
        if os.path.isdir(srcPath):
            if file in dirName.values():
                continue
            elif '현미경' in file:
                continue
            else:
                # 해당 파일이 폴더라면 재귀
                fileList(srcPath)
        else:
            if '-' not in file:
                continue
            filePos = int(file.split('-')[-1].split('.')[0])
            dstPath = os.path.join(dir_name,dirName[filePos])
            if not (os.path.isdir(dstPath)):
                os.mkdir(dstPath)
            dstPath = os.path.join(dstPath,file)
            # 파일 옮기기
            shutil.move(srcPath, dstPath)
            #print(fileName)


fileList(path)
