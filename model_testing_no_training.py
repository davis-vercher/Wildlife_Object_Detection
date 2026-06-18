from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo26n.pt")

# Perform object detection on an image
results = model("C:/Users/Dave/Desktop/0037.jpg")

# Visualize the results
for result in results:
    result.show()