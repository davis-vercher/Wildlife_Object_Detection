from PIL import Image
import os

# Folder to scan
input_folder = r"D:\wildlife_yolo_project_20250619\test_all_resized"

# Store unique sizes in a set
unique_sizes = set()

for filename in os.listdir(input_folder):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
        continue  # skip unsupported file types

    try:
        image_path = os.path.join(input_folder, filename)
        with Image.open(image_path) as img:
            unique_sizes.add(img.size)  # (width, height)
    except Exception as e:
        print(f"Error reading {filename}: {e}")

# Print results
print("Unique image sizes found:")
for size in sorted(unique_sizes):
    print(f"{size[0]} x {size[1]}")
