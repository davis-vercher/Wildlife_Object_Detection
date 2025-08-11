from PIL import Image, ImageOps
import os

# Input and output folders
input_folder = r"D:\wildlife_yolo_project_20250619\test_all"
output_folder = r"D:\wildlife_yolo_project_20250619\test_all_resized"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
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

    else:
        print(f"{filename}: skipped (size {width}x{height})")
        continue

    output_path = os.path.join(output_folder, filename)
    resized.save(output_path)

print("Done processing all images.")
