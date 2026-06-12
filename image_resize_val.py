from PIL import Image
import os

input_folder = r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\small_imageset_500_deer_hog_coyote\deer"

unique_sizes = set()

for filename in os.listdir(input_folder):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
        continue

    try:
        image_path = os.path.join(input_folder, filename)
        with Image.open(image_path) as img:
            unique_sizes.add(img.size)
    
    except Exception as e:
        print(f"Error reading {filename}: {e}")


print("Unique image sizes found:")
for size in sorted(unique_sizes):
    print(f"{size[0]} x {size[1]}")
