"""
Purpose:
Using the base YOLO 26 model to spot-predict on individual images.

This is a simple test of the base YOLO 26 model (not trained on the wildlife dataset)
to see how it performs at object detection predictions on wild hog, deer, and coyote images
on the local machine.
"""

from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo26n.pt")

# Perform object detection on an image
results = model("C:/[input actual path]/<your_single_image>.jpg")

# Visualize the results
for result in results:
    result.show()