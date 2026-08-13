"""
Purpose:
Convert label files/folder structure from YOLO format to Label-Studio format.
"""

import os
import json
from PIL import Image

BASE_DIR = r"C:[input actual path]\Wildlife_Object_Detection\model\500_imageset_model\small_imageset"
IMAGES_DIR = os.path.join(BASE_DIR, "images")
LABELS_DIR = os.path.join(BASE_DIR, "labels")
OUTPUT_JSON = os.path.join(BASE_DIR, "predictions.json")

# Must match your Label Studio labeling config
FROM_NAME = "label"
TO_NAME = "image"

# Every YOLO box will be imported as this label
DEFAULT_LABEL = "Animal"

# This must match your Label Studio local files document root setup
IMAGE_URL_PREFIX = "/data/local-files/?d=images%5C"

tasks = []

for image_file in sorted(os.listdir(IMAGES_DIR)):
    if not image_file.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image_path = os.path.join(IMAGES_DIR, image_file)
    label_file = os.path.splitext(image_file)[0] + ".txt"
    label_path = os.path.join(LABELS_DIR, label_file)

    with Image.open(image_path) as img:
        img_width, img_height = img.size

    results = []

    if os.path.exists(label_path):
        with open(label_path, "r") as f:
            lines = f.readlines()

        for line in lines:
            parts = line.strip().split()

            if len(parts) < 5:
                continue

            # Ignore class_id
            _, x_center, y_center, box_width, box_height = parts[:5]

            x_center = float(x_center)
            y_center = float(y_center)
            box_width = float(box_width)
            box_height = float(box_height)

            # Convert YOLO normalized coords to Label Studio percentage coords
            x = (x_center - box_width / 2) * 100
            y = (y_center - box_height / 2) * 100
            width = box_width * 100
            height = box_height * 100

            results.append({
                "from_name": FROM_NAME,
                "to_name": TO_NAME,
                "type": "rectanglelabels",
                "value": {
                    "x": x,
                    "y": y,
                    "width": width,
                    "height": height,
                    "rotation": 0,
                    "rectanglelabels": [DEFAULT_LABEL],
                }
            })

    task = {
        "data": {
            "image": f"{IMAGE_URL_PREFIX}{image_file}"
        },
        "predictions": [
            {
                "model_version": "yolo26n_boxes_only",
                "score": 0.5,
                "result": results
            }
        ]
    }

    tasks.append(task)

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(tasks, f, indent=2)

print(f"Created: {OUTPUT_JSON}")
print(f"Images processed: {len(tasks)}")