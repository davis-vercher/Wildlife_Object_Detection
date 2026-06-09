import os

source_folder = r"D:\wildlife_yolo_project_20250619\test_all_resized"

files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

files.sort()

processed = 0
max_images = 10000

for i, filename in enumerate(files, 1):
    if processed >= max_images:
        break
    
    ext = os.path.splitext(filename)[1]
    new_filename = f"{i:04d}{ext.lower()}"

    if filename == new_filename:
        print(f"Skipped: {filename} already correct.")
        processed += 1
        continue

    old_path = os.path.join(source_folder, filename)
    new_path = os.path.join(source_folder, new_filename)
    
    if os.path.exists(new_path):
        print(f"Skipped: {filename} already correct.")
        processed += 1
        continue

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_filename}")
    processed += 1

print(f"Complete: Renamed {processed} files.")
