import paddlehub
import time

# face = paddlehub.Module(name="pyramidbox_lite_mobile_mask")
# face = paddlehub.Module(name="pyramidbox_lite_mobile")
# face = paddlehub.Module(name="pyramidbox_lite_server_mask")
# face = paddlehub.Module(name="pyramidbox_lite_server")
# face = paddlehub.Module(name="pyramidbox_face_detection")
face = paddlehub.Module(name="ultra_light_fast_generic_face_detector_1mb_640")

image = ["images/testd.jpg"]

time_start = time.process_time()
results = face.face_detection(data={"image": image})
time_end = time.process_time()

# print(results)
print(time_end - time_start)
