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
