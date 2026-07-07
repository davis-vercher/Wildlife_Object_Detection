"""
Purpose:
Train the base YOLO 26 model on the small wildlife imageset.
"""


from ultralytics import YOLO
import torch

print("=" * 50)
print(f"PyTorch Version: {torch.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"GPU Count: {torch.cuda.device_count()}")
    print(f"Current GPU: {torch.cuda.get_device_name(0)}")
    print(f"CUDA Version: {torch.version.cuda}")
else:
    raise RuntimeError(
        "CUDA is not available. Training aborted to prevent CPU training."
    )

print("=" * 50)

model = YOLO("yolo26n.pt")

model.train(
    data=r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\small_imageset\wildlife.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    workers=0,
    name="wildlife_yolo26n"
)

print("Training complete")