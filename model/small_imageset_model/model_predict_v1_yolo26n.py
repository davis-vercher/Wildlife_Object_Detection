from ultralytics import YOLO

model = YOLO(r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\runs\detect\wildlife_yolo26n\weights\best.pt")

results = model("C:/Users/Dave/Desktop/pig.jpg")

for result in results:
    result.show()