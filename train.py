
from ultralytics import YOLO

model = YOLO("yolov8-seg.yaml").load("yolov8n.pt")

results = model.train(data="coco8-seg.yaml", epochs=100, imgsz=640)

model.export()