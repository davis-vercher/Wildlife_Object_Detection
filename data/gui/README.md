#### This folder was generated with Codex as a prototype

# JPEG Dataset Sorter

A local Windows desktop app for reviewing JPEG images one at a time and moving
them into class folders with the number keys `0` through `9`.

## Setup

1. First, double-click `run_jpg_sorter.bat`. It will use a compatible local
   Python installation automatically when one is available.
2. If the launcher reports a missing dependency, install Python 3 for Windows
   from python.org. During installation, enable **Add Python to PATH**.
3. Open Command Prompt in this folder and install the one image-display
   dependency:

       python -m pip install -r requirements.txt

4. Double-click `run_jpg_sorter.bat` again.

The application does not connect to the internet. Pillow is used only to decode
and resize local JPEG images inside the GUI.

## Use

1. Select the source folder containing `.jpg` or `.jpeg` files.
2. Give each class a name and assign its destination folder to a number key.
   Each folder may be assigned to only one key.
3. Select **Start**.
4. Press an assigned number key, or click its on-screen button, to move the
   displayed image into that destination. The number-key legend remains visible
   below the image as a reminder of every assigned class name.
5. Select **Undo last move** to restore only the most recently moved image to
   the source folder. The restored image is displayed again immediately.

The app processes files in alphabetical filename order. It never overwrites an
existing destination file: if a name is already taken, `_1`, `_2`, and so on is
added to the moved filename. Folder choices are saved locally in
`sorter_config.json` after Start is selected.
