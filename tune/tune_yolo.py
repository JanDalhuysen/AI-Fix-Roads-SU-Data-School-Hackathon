# import torch

# Load a pre-trained YOLOv8 model
# model = torch.hub.load('ultralytics/yolov8', 'yolov8n-seg')  # Or choose another model

from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Load a model from a file

# Prepare your dataset (assuming it's in COCO format)
train_path = '.\\train\\images'
val_path = '.\\val\\images'

# Fine-tune the model
results = model.train(
    data='pothole.yaml',
    epochs=10
)
