"""
Purpose:
Using the best YOLO 26 model to spot-predict on individual images.

This is a simple test of the best YOLO 26 model (trained on the small wildlife dataset)
to see how it performs at object detection predictions on wild hog, deer, and coyote images
on the local machine.
"""

from ultralytics import YOLO

model = YOLO(r"C:[input actual path]\Wildlife_Object_Detection\runs\detect\wildlife_yolo26n\weights\best.pt")

results = model("C:/[input actual path]/<your_single_image>.jpg")

for result in results:
    result.show()