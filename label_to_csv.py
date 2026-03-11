import os
import csv

scan_folder_path = r"C:\Users\Personal\Documents\Wildlife Object Detection Project 2025-2026\Archive\project-1-at-2026-03-01-12-41-76bc6933\test_labels"
output_folder_path = r"C:\Users\Personal\Documents\Wildlife Object Detection Project 2025-2026"

csv_name = "file_list_labelsfolder.csv"

output_csv = os.path.join(output_folder_path, csv_name)

os.makedirs(output_folder_path, exist_ok=True)

with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    for root, dirs, files in os.walk(scan_folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            writer.writerow([file])

print(f"CSV file created at: {output_csv}")