from ultralytics import YOLO

model = YOLO(r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\runs\detect\wildlife_yolo26n\weights\best.pt")

model.predict(
    source=r"C:\Users\Dave\Desktop\0037.jpg",
    conf=0.25,
    save=True
)
