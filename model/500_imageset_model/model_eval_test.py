"""
Purpose:
Test the best YOLO26n model after the initial 100 epochs of training on the test set.

Output:
Outputs the standard Ultralytics .png and .jpg results of the testing, prints the precision, recall,
mAP50, and mAP50-95 results to the terminal, and a CSV file of the same four metrics.
"""

from ultralytics import YOLO
import csv

model = YOLO(
    r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\model\500_imageset_model\runs\detect\wildlife_yolo26n\weights\best.pt"
)

metrics = model.val(
    data=r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\model\500_imageset_model\small_imageset\wildlife.yaml",
    split="test",
    imgsz=640,
    batch=16,
    workers=0,
    project=r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\model\500_imageset_model\runs\detect",
    name="wildlife_yolo26n_test"
)

out_path = r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\model\500_imageset_model\runs\detect\wildlife_yolo26n_test\test_metrics.csv"

with open(out_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["precision", "recall", "mAP50", "mAP50-95"])
    writer.writerow([
        metrics.box.mp,
        metrics.box.mr,
        metrics.box.map50,
        metrics.box.map,
    ])

print(f"Precision: {metrics.box.mp:.2f}")
print(f"Recall: {metrics.box.mr:.2f}")
print(f"mAP50: {metrics.box.map50:.2f}")
print(f"mAP50-95: {metrics.box.map:.2f}")