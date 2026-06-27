# Small Imageset - First Model
This folder houses all work done to get to the first trained YOLO 26 (nano) model on the small 500 images dataset.

### Dataset
The "small_imageset" folder contains .jpg images and .txt class/bounding box labels for 500 images in three classes:
- Coyote (27 images)
- White-Tailed Deer (229 images)
- Wild Hog (244 images)

Both the \images and \labels folders are split into \train, \val, and \test folders. There are 398 training images/labels, 51 validation images/labels, and 51 test images/labels.

Each .jpg image corresonds to an identically named .txt label file (i.e., "0213.jpg" corresponds to "0213.txt").

### Model
The model selected is a YOLO 26 nano model, and is trained in "model_training_v1_yolo26n.py".

The YOLO model.train() parameters used are:
- epochs = 100
- imgsz = 640
- batch = 16
- workers = 0

The best model from this initial training run is stored in ..\runs\detect\wildlife_yolo26n\weights\best.pt