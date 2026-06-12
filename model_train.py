"""
# Below is for testing CUDA availabilty/integration with PyTorch for local machine
import torch

print(f"Is CUDA available?: {torch.cuda.is_available()}")
print(f"PyTorch CUDA version: {torch.version.cuda}")
print(f"Device Name: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")
"""

from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo26n.pt")

# Perform object detection on an image
results = model("C:/Users/Dave/Desktop/0037.jpg")

# Visualize the results
for result in results:
    result.show()