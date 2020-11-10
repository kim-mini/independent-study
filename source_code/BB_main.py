import numpy as np
import cv2
import os
import datetime
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from calibration import calib, undistort
from threshold import gradient_combine, hls_combine, comb_result
from finding_lines import Line, warp_image, find_LR_lines, draw_lane, print_road_status, print_road_map
import shutil
from skimage import exposure

input_name = 'project_video.mp4' #'test_images/straight_lines1.jpg' # 'challenge_video.mp4'

left_line = Line()
right_line = Line()

th_sobelx, th_sobely, th_mag, th_dir = (35, 100), (30, 255), (30, 255), (0.7, 1.3)
th_h, th_l, th_s = (10, 100), (0, 60), (85, 255)

# camera matrix & distortion coefficient
mtx, dist = calib()
now = datetime.datetime.now().strftime("%d_%H-%M-%S")

outpath = "/home/ubuntu/PycharmProjects/laneDetect/blackbox_project/output"#저장될 주소

if not os.path.isdir(outpath):  # 해당경로 디렉토리가 없다면 만들어라
    os.mkdir(outpath)

filelist = os.listdir(outpath)


frameRate = 25 #video FPS
fourcc = cv2.VideoWriter_fourcc(*'mp4v')#video codec

record = 0 # record status



# def useDisk(a, b):
#     if a+2000000

diskLabel = outpath#사용량 체크
_, used, _ = shutil.disk_usage(diskLabel)
print('1',used)

if __name__ == '__main__':

    cap = cv2.VideoCapture(input_name)

    while (cap.isOpened()):
        _, frame = cap.read()

        # Correcting for Distortion
        undist_img = undistort(frame, mtx, dist)
        # resize video
        undist_img = cv2.resize(undist_img, None, fx=1 / 2, fy=1 / 2, interpolation=cv2.INTER_AREA)
        rows, cols = undist_img.shape[:2]

        combined_gradient = gradient_combine(undist_img, th_sobelx, th_sobely, th_mag, th_dir)
        # cv2.imshow('gradient combined image', combined_gradient)

        combined_hls = hls_combine(undist_img, th_h, th_l, th_s)
        #cv2.imshow('HLS combined image', combined_hls)

        combined_result = comb_result(combined_gradient, combined_hls)

        c_rows, c_cols = combined_result.shape[:2]
        s_LTop2, s_RTop2 = [c_cols / 2 - 24, 5], [c_cols / 2 + 24, 5]
        s_LBot2, s_RBot2 = [110, c_rows], [c_cols - 110, c_rows]

        src = np.float32([s_LBot2, s_LTop2, s_RTop2, s_RBot2])
        dst = np.float32([(170, 720), (170, 0), (550, 0), (550, 720)])

        warp_img, M, Minv = warp_image(combined_result, src, dst, (720, 720))
        # cv2.imshow('warp', warp_img)

        searching_img = find_LR_lines(warp_img, left_line, right_line)
        # cv2.imshow('LR searching', searching_img)

        w_comb_result, w_color_result = draw_lane(searching_img, left_line, right_line)
        # cv2.imshow('w_comb_result', w_comb_result)

        # Drawing the lines back down onto the road
        color_result = cv2.warpPerspective(w_color_result, Minv, (c_cols, c_rows))
        lane_color = np.zeros_like(undist_img)
        lane_color[220:rows - 12, 0:cols] = color_result

        # Combine the result with the original image
        result = cv2.addWeighted(undist_img, 1, lane_color, 0.3, 0)
        # cv2.imshow('result', result.astype(np.uint8))

        info, info2 = np.zeros_like(result), np.zeros_like(result)
        info[5:110, 5:190] = (255, 255, 255)
        info2[5:110, cols - 111:cols - 6] = (255, 255, 255)
        info = cv2.addWeighted(result, 1, info, 0.2, 0)
        info2 = cv2.addWeighted(info, 1, info2, 0.2, 0)
        road_map = print_road_map(w_color_result, left_line, right_line)
        info2[10:105, cols - 106:cols - 11] = road_map
        info2 = print_road_status(info2, left_line, right_line)
        cv2.imshow('road info', info2)




        if not(record) : #record = False
            record += 1

            h, w = info2.shape[:2]  # 이미지의 h,w을 넘겨줄때는 채널넘겨주지 않도록 주의
            c_cols, c_rows = combined_result.shape[:2]

            frame_size = w, h
            frame_size2 = c_rows, c_cols

            outname = os.path.join(outpath, "info2_{}.mp4".format(now))
            outname2 = os.path.join(outpath, "combient_{}.mp4".format(now))

            out = cv2.VideoWriter(outname, fourcc, frameRate, frame_size)
            out2 = cv2.VideoWriter(outname2, fourcc, frameRate, frame_size2, 0)

        if record:#위에서 +1을 해줘서 이쪽으로 들어온다 그리곤 녹화
            out.write(info2)
            out2.write(combined_result)

        if (cap.get(cv2.CAP_PROP_POS_FRAMES)) % 250 == 0:#10초가 지났으면 영상을 끊고 다시 시작함
            out.release()
            out2.release()
            now = datetime.datetime.now().strftime("%d_%H-%M-%S")
            outname = os.path.join(outpath, "info2_{}.mp4".format(now))
            outname2 = os.path.join(outpath, "combient_{}.mp4".format(now))

            out = cv2.VideoWriter(outname, fourcc, frameRate, frame_size)
            out2 = cv2.VideoWriter(outname2, fourcc, frameRate, frame_size2, 0)
            record -= 1

            diskLabel2 = outpath
            _, used2, _ = shutil.disk_usage(diskLabel2)
            print('2', used2)
            if (used + 10000000)>used2:
                for file in filelist:


        #out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.waitKey(0)
        # if cv2.waitKey(1) & 0xFF == ord('r'):
        #    cv2.imwrite('check1.jpg', undist_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


    print(filelist)

