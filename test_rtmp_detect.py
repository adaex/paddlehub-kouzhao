import cv2
import os
import time
import paddlehub as hub
import random

ROOT_DIR = 'cv_detection'
RTMP_SERVER = 'rtmp://192.168.10.164:18102/live/livestream'
SKIP_FRAMES = 150
# ROOT_DIR = os.environ["ROOT_DIR"]
# RTMP_SERVER = os.environ["RTMP_SERVER"]
# SKIP_FRAMES = os.environ.get('SKIP_FRAMES') or '9'

print('RTMP_SERVER', RTMP_SERVER)
print('ROOT_DIR', ROOT_DIR)
print('SKIP_FRAMES', SKIP_FRAMES)


def generate_dir(dirName):
    try:
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        return dirName

    except OSError as err:
        print('Error: Creating directory of data', err)


generate_dir(ROOT_DIR)
cap = cv2.VideoCapture(RTMP_SERVER)
module = hub.Module(name="pyramidbox_lite_server_mask")


def skip_frames(_cap, count=int(SKIP_FRAMES)):
    while count > 0:
        success = _cap.grab()
        if not success:
            print('skip_frames success', success)
            return
        count -= 1


def face_detect(_input_dict):
    results = module.face_detection(data=_input_dict)
    # for result in results:
    #     print(result)
    return [len(results) > 0, results]


current_milli_time = lambda: int(round(time.time() * 1000))

mock_35_36 = lambda: round(random.randrange(350, 360, 1))
mock_36_37 = lambda: round(random.randrange(360, 370, 1))
mock_37_38 = lambda: round(random.randrange(370, 380, 1))
mock_38_40 = lambda: round(random.randrange(380, 400, 1))


def mock_temperature():
    num = random.random() * 10
    if num < 4:
        temperature = mock_35_36()
    elif num < 7:
        temperature = mock_36_37()
    elif num < 9:
        temperature = mock_37_38()
    else:
        temperature = mock_38_40()
    return temperature


errNo = 1

while True:
    time1 = time.time()
    ret, frame = cap.read()
    time2 = time.time()

    if ret:
        input_dict = {"data": [frame]}
        time3 = time.time()
        [detectResult, faces] = face_detect(input_dict)
        time4 = time.time()

        # print('read', time2 - time1, 'detect', time4 - time3, )

        if detectResult is True:
            timestamp = current_milli_time()

            time4 = time.time()

            for i in range(len(faces)):
                temperature = mock_temperature()
                file = str(timestamp) + '_' + str(temperature)
                full_file = ROOT_DIR + '/' + file

                face = faces[i]
                left = round(face['data']['left'])
                right = round(face['data']['right'])
                top = round(face['data']['top'])
                bottom = round(face['data']['bottom'])

                width = int((right - left) / 2)
                height = int((bottom - top) / 2)

                cv2.imwrite(full_file + '_' + '{:03d}'.format(i) + '.jpg',
                            frame[top - width:bottom + width, left - height:right + height])

                data = {
                    "url": 'detection/' + file + '_' + '{:03d}'.format(i) + '.jpg',
                    "face": faces[i],
                    "temperature": temperature,
                    "timestamp": timestamp
                }

                fo = open(full_file + '_' + '{:03d}'.format(i) + '.json', "w")
                fo.write(str(data))
                fo.close()

            time5 = time.time()
            # print('write', time5 - time4)

        skip_frames(cap)

    else:
        time.sleep(1)
        print('wait up to ', errNo)
        errNo += 1
        if errNo == 30:
            break

# Release all space and windows once done
cap.release()
cv2.destroyAllWindows()
