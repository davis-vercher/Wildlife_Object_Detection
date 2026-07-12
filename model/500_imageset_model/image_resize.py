"""
Purpose:
This file converts the wildlife trail camera images from three specific sizes into one compatible size.

Input Sizes Accepted:
- 1920 x 1080
- 2048 x 1536
- 640 x 360

Output Size:
- 640 x 360
"""

from PIL import Image, ImageOps
import os

# Input and output folders
input_folder = r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\small_imageset_500_deer_hog_coyote\deer"
output_folder = r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\small_imageset_500_deer_hog_coyote\deer_resized"
os.makedirs(output_folder, exist_ok=True)

skipped_files = []
processed = 0
max_images = 1000

for filename in os.listdir(input_folder):
    if processed >= max_images:
        break
    
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        print(f"Skipping {filename}: unsupported file type")
        continue

    image_path = os.path.join(input_folder, filename)
    image = Image.open(image_path)
    width, height = image.size

    if (width, height) == (1920, 1080):
        resized = image.resize((640, 360), Image.Resampling.LANCZOS)
        print(f"{filename}: resized from 1920x1080 to 640x360")

    elif (width, height) == (2048, 1536):
        resized = image.resize((480, 360), Image.Resampling.LANCZOS)
        delta_w = 640 - 480
        padding = (delta_w // 2, 0, delta_w - (delta_w // 2), 0)
        resized = ImageOps.expand(resized, padding, fill=(0, 0, 0))
        print(f"{filename}: resized from 2048x1536 to 480x360, then padded to 640x360")

    elif (width, height) == (640, 360):
        resized = image
        print(f"{filename}: no resizing needed for size ({width}x{height})")

    else:
        resized = image
        print(f"{filename}: skipped (size {width}x{height}) ---------------------------------------------")
        skipped_files.append(filename)
        continue

    output_path = os.path.join(output_folder, filename)
    resized.save(output_path)
    processed += 1


print("Done processing all images.")
print(f"\nSkipped {len(skipped_files)} files:")
if skipped_files:
    for file in skipped_files:
        print(f"  - {file}")
else:
    print("  No files skipped.")
