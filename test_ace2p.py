import paddlehub as hub

ace2p = hub.Module(name="ace2p")

image = ["images/1.jpg"]

results = ace2p.segmentation(data={"image": image})

# print(results)
