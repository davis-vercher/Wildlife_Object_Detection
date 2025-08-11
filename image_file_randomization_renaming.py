import os
import random
import shutil

# Source folder (original images)
source_folder = r"D:\wildlife_yolo_project_20250619\test_all"

# Destination folder (randomized and renamed)
destination_folder = r"D:\wildlife_yolo_project_20250619\test_all_shuffled"
os.makedirs(destination_folder, exist_ok=True)

# Get list of files
files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# Shuffle the list
random.shuffle(files)

# Copy and rename
for i, filename in enumerate(files, 1):
    ext = os.path.splitext(filename)[1]
    new_name = f"{i:04}{ext.lower()}"
    src_path = os.path.join(source_folder, filename)
    dst_path = os.path.join(destination_folder, new_name)
    shutil.copy2(src_path, dst_path)  # copy2 keeps metadata

print("Images copied and renamed successfully.")
