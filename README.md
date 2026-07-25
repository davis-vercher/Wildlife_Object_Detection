# Wildlife Object Detection
This is a personal project conducted to get hands on learning experience with creating a real-time object detection pipeline, and covers:
- Image web scraping to build the image dataset
    - Selenium
    - Label-Studio
    - GCP Buckets
- Transfer learning with the YOLO family of models
    - YOLO 26
    - PyTorch
- MVP of a real-time object detection model used in a live environment (local machine browser)
    - OpenCV
    - MSS
    - PyQT5


## (Phase 1) Small Imageset - First Model
The initial phase of work for this project is using a small, MVP imageset to train the initial model. This preliminary model will be used in the MVP real-time object detection browser application.

### Dataset
The "small_imageset" folder contains .jpg images and .txt class/bounding box labels for 500 images in three classes:
- Coyote [27 images: {train: 20}, {val: 3}, {test: 4}]
- White-Tailed Deer [229 images: {train: 210}, {val: 23}, {test: 28}]
- Wild Hog [244 images: {train: 449}, {val: 31}, {test: 26}]
- Piglet [73 images: {train: 70}, {val: 0}, {test: 3}]

Both the \images and \labels folders are split into \train, \val, and \test folders. There are 398 training images/labels, 51 validation images/labels, and 51 test images/labels.

Each .jpg image corresonds to an identically named .txt label file (i.e., "0213.jpg" corresponds to "0213.txt").

### Model
The model selected is a YOLO 26 nano model, and is trained in "model_training_v1_yolo26n.py".

The YOLO model.train() parameters used are:
- epochs = 100
- imgsz = 640
- batch = 16
- workers = 0

The best model from this initial training run is stored in:
..\model\500_imageset_model\runs\detect\wildlife_yolo26n\weights\best.pt

### Results
After one 100 epoch round of training the base yolo26n model results are:
- Precision: 0.9266
- Recall:    0.8465
- mAP50:     0.8625
- mAP50-95:  0.6529

And results of the best model on the test images are:
- Precision: 0.9701
- Recall:    0.6585
- mAP50:     0.6681
- mAP50-95:  0.4941

Anecdotally, the model fails to detect coyote and piglet images, struggles to detect deer (and confuses deer with humans), and performs moderately at hog detection.

When using 'yolo_openCV_overlay.py' (..\detect\.) to run the model on a live feed of the local screen, the model performs best for hog images (when using a browser to search for images of "wild hogs in the wild"), and performs poorly for the other classes.


### Lessons Learned
#### Overall Thoughts
The imageset was too small to be meaningful, additional classes are needed, & improving the dataset needs to take priority over experimenting with different YOLO model sizes/configurations.

#### Detailed Problems
The imageset has several key issues:
- *Imbalance of Classes:* Smaller classes (coyote, piglet) were significantly smaller than the Hog and Deer classes. This can be addressed by gathering more instances of these classes and by using data augmentation on the existing images.
- *Error in Class Splits:* The piglet set has zero instances in the validation split. This was caused by an oversight when creating the splits. Originally I intended there to not be a 'piglet' class seperate from 'Hog' but due to the moderate quantity of piglet instances in hog images (piglets are almost always with their adult mother/sounder in the wild, and therefore were in the images with adult hogs), I created a seperate piglet class. Also, piglets are visually distinct in many cases than adult hogs (presence of spots, striping, and lighter fur color).
- *Small Size:* The overall small size of the total imageset made for fast manual annotations, but has proven after one training run to be too small.

The goal of this project needs to be refined:
- *Goal To-Date:* Get a YOLO model trained on local hardware with local images for the first time
- *Refined Goal:* Build a field-ready detector of wild hogs/piglets that never confuses images of deer, dogs, cows, humans for hogs, and also does not confuse wild background (trees moving, grass moving, shadows, etc.) for hogs.
This refinement will narrow my next iteration of training to focus on creating a boundary specifically for hogs vs not hogs in images, rather than detecting each class successfully


#### Next Steps
- 1) Create a larger dataset of ~1,250-1,500 images with the following classes:
    - Hog: 350
    - Piglet: 100
    - Deer: 250
    - Dog: 150
    - Human: 150
    - Coyote: 100
    - Cow: 150
    - Empty: 250
- 2) Figure out a less manual pipeline that can be public facing (i.e., not putting my local paths in files, not having multiple files that each do one small thing, creating repeatable configurations/runs with yaml files, etc.)

## (Phase 2) Enhancing the initial imageset
The second phase of work for this project will focus on enhancing the size and quality of the imageset to fix the issues identified in Phase 1.
