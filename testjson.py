import json
from collections import defaultdict
import os

tasks_file = r"C:\Users\Personal\Documents\Wildlife Object Detection Project 2025-2026\tasks.json"
labels_folder = r"C:\Users\Personal\Documents\Wildlife_Object_Detection\yolov8_7Mar26\labels"

# Load the JSON file
with open(tasks_file, "r") as f:
    tasks = json.load(f)


# Creating hashmap to store correctly formated task ID with corresponding .jpg image file
res = defaultdict(list)

for task in tasks[:10]:
    raw_task_id = str(task["id"])
    if len(raw_task_id) == 4:
        continue
    elif len(raw_task_id) == 3:
        task_id = str("0" + raw_task_id)
    elif len(raw_task_id) == 2:
        task_id = str("00" + raw_task_id)
    elif len(raw_task_id) == 1:
        task_id = str("000" + raw_task_id)

    image_name = str((task["data"]["image"])[-8:])
    
    res[task_id].append(image_name)

#print(res)

# Process every label file
for file in os.listdir(labels_folder):

    if not file.endswith(".txt"):
        continue

    

