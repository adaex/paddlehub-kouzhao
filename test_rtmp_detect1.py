import cv2
import os
import time
import paddlehub as hub
import random

ROOT_DIR = 'cv_detection'
RTMP_SERVER = 'rtmp://192.168.10.164:18102/live/livestream'
SKIP_FRAMES = 150

cap = cv2.VideoCapture(RTMP_SERVER)



while True:

    ret, frame = cap.read()
    # 就是个处理一帧的例子，这里转为灰度图
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 不断显示一帧，就成视频了
    # 这里没有提前创建窗口，所以默认创建的窗口不可调整大小
    # 可提前使用cv.WINDOW_NORMAL标签创建个窗口
    if ret:
        cv2.imshow('frame', frame)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# cap.release()
# cv2.destroyAllWindows()
