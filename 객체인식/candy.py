import yaml

data = {
    'train' : 'dataset/train/',
    'val' : 'dataset/valid/',
    'test' : 'dataset/test/',
    'names' : {0 : 'candy'}
}

with open('./candy.yaml', 'w') as f:
    yaml.dump(data, f)
    
with open('./candy.yaml', 'r') as f:
    lines = yaml.safe_load(f)
    print(lines)

'''
from ultralytics import YOLO

model = YOLO('yolov8s.pt')
model.train(data = './candy.yaml', epochs = 20)
'''