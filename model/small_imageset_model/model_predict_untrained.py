"""
Purpose:
Create bounding box annotations (with predictions) on the small wildlife imageset to make
annotating in label-studio faster.

Reason:
Using the base YOLO 26 model (not trained on the data), predictions (bounding boxes, labels) are applied
to all images in the small wildlife imageset. These predictions can be uploaded in label-studio and
applied to the corresponding images.
"""

from ultralytics import YOLO
from pathlib import Path

model = YOLO("untrained_yolo26n.pt")

base_dir = Path(
    r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\small_imageset"
)

folders = [
    "images"
]

for folder in folders:
    source_dir = base_dir / folder

    print(f"Processing {source_dir}...")

    model.predict(
        source=str(source_dir),
        save=True,          # save images with boxes drawn
        save_txt=True,      # save YOLO predictions
        save_conf=True,     # save confidence scores
        conf=0.25,          # confidence threshold
        project="prediction_results",
        name=folder,
        exist_ok=True,
        verbose=True
    )

print("Done!")