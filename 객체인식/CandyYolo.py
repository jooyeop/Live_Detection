from ultralytics import YOLO

model = YOLO('yolov8s.pt')
model.train(data = './candy.yaml', epochs = 20)