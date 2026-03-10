import json
from collections import defaultdict
import os

tasks_file = r"C:\Users\Personal\Documents\Wildlife Object Detection Project 2025-2026\tasks.json"
labels_folder = r"C:\Users\Personal\Documents\Wildlife Object Detection Project 2025-2026\Archive\project-1-at-2026-03-01-12-41-76bc6933\test_labels"

# Load the JSON file
with open(tasks_file, "r") as f:
    tasks = json.load(f)


# Creating hashmap to store correctly formated task ID with corresponding .jpg image file
res = defaultdict(list)

for task in tasks:
    raw_task_id = str(task["id"])
    if len(raw_task_id) == 4:
        task_id = str(raw_task_id)
    elif len(raw_task_id) == 3:
        task_id = str("0" + raw_task_id)
    elif len(raw_task_id) == 2:
        task_id = str("00" + raw_task_id)
    elif len(raw_task_id) == 1:
        task_id = str("000" + raw_task_id)

    image_name = str((task["data"]["image"])[-8:-4])
    
    res[task_id].append(image_name)


# Process every label file
for file in os.listdir(labels_folder):

    if not file.endswith(".txt"):
        continue

    file_name = file[-8:-4]
    new_name = res[file_name][0] + ".txt"

    old_path = os.path.join(labels_folder, file)
    new_path = os.path.join(labels_folder, new_name)

    if not os.path.exists(new_path):
        os.rename(old_path, new_path)
        print(file, " --> ", new_name)
    else:
        print("Skipping (already exists): ", new_name)