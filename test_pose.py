import paddlehub as hub

pose = hub.Module(name="pose_resnet50_mpii")

image = ["images/1.jpg"]

results = pose.keypoint_detection(data={"image": image})

# print(results)
