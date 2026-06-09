import json
import os
import shutil

labels_folder = r"C:\Users\Personal\Documents\Wildlife_Object_Detection\yolov8_7Mar26\labels"
images_folder = r"D:\wildlife_yolo_project_20250619\deer_hog_coyote_5384images_20250816"
tasks_file = r"C:\Users\Personal\Documents\Wildlife_Object_Detection\tasks.json"

with open(tasks_file) as f:
    tasks = json.load(f)

# Build mapping
id_to_image = {}

for task in tasks:
    task_id = str(task["id"])
    image_name = os.path.basename(task["data"]["image"])
    id_to_image[task_id] = os.path.splitext(image_name)[0]

# Process every label file
for file in os.listdir(labels_folder):

    if not file.endswith(".txt"):
        continue

    task_id = file.split("_")[-1].replace(".txt","")

    if task_id in id_to_image:

        new_name = id_to_image[task_id] + ".txt"

        old_path = os.path.join(labels_folder, file)
        new_path = os.path.join(labels_folder, new_name)

        shutil.move(old_path, new_path)

        print(file, "→", new_name)

    else:
        print("Task ID not found for:", file)