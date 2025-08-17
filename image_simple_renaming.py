import os

source_folder = r"D:\wildlife_yolo_project_20250619\test_test"

files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

processed = 0
max_images = 10

for i, filename in enumerate(files, 1):
    if processed >= max_images:
        break
    
    ext = os.path.splitext(filename)[1]
    new_filename = f"{i:04}{ext.lower()}"
    
    old_path = os.path.join(source_folder, filename)
    new_path = os.path.join(source_folder, new_filename)

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_filename}")

    processed += 1

print(f"Complete: Renamed {len(files)} files.")
