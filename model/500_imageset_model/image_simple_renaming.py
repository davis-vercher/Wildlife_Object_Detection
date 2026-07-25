"""
Purpose:
Rename all files in a single folder to a sequential numerical structure, keeping the file extension.

Renaming Structure:
0001.jpg, 0002.jpg, 0003.jpg ... NNNN.jpg (where NNNN is the final number in the sequence)
"""

import os

source_folder = r"C:[input actual path]\Wildlife_Object_Detection\[input actual path]"

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