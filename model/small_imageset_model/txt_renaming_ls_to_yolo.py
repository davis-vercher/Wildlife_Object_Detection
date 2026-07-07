"""
Purpose:
Rename label files from Label-Studio outputs to YOLO format.

Reason:
When exporting annotations from label-studio, the file name ends with the four-digit
code corresponding to the image for the annotations (i.e., 0001.jpg and 0001.txt). 
However, label-studio adds a string of text before the four-digit code to the front
of the .txt file.

Input:
(example) sdake302ac0001.txt

Output
(example) 0001.txt
"""

import os

labels_directory = r"C:\Users\Dave\Documents\robotics_project\Wildlife_Object_Detection\small_imageset\test_labels"

for filename in os.listdir(labels_directory):
    image_num = filename[-8:-4]

    new_filename = f"{image_num}.txt"

    if filename == new_filename:
        print(f"Skipped: {filename} already correct.")
        continue

    old_path = os.path.join(labels_directory, filename)
    new_path = os.path.join(labels_directory, new_filename)

    os.rename(old_path, new_path)

    print(f"Rename: {filename}  -->  {image_num}.txt")
