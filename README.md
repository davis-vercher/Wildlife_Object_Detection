# Wildlife_Object_Detection

## 1. Project Overview
#### 1A. Purpose
Create a computer vision (CV) model that accurately detects wild hogs in a live video feed. This model will be used in a robotics platform that will automatically aim and "fire" a laser aiming device at the hog.

#### 1B. Description
Create a CV model that can accurately detect wild hogs while accurately avoiding visually similar animals (i.e., Whitetail Deer, large dogs).

#### 1C. Goals
- Create a model that can succesfully identify wild hogs while successfully avoid false positive identification on deer, dogs, people, etc.
- Create a model that is usable on an edge robotics laser aiming system
- Create functionality where the model can also predict how lethal a simulated rifle round (laser) would be if fired at a specific point on the hog // accounting for foliage occlusion, round placement, etc.

#### 1D. MVP (Phase 0)
Use an out of the box (OOTB) yolo model without training on a set of annotated wild hog images.
- Record results (investigation needed into learning proper ML model results reporting - i.e., AUC/ROC curve, TP FP TN FN matrix, etc.)

#### 1E. Phase 1
Create an annotated image dataset of wild hog images (~1,000) using label-studio.
- Setup label-studio to pull from GCP bucket of raw images
- Annotate using label-studio (needs investigation in bounding boxes vs AI-augmented shape outline annotation)
- Export in-stream annotations to second GCP bucket
- Train yolo model on wild hog dataset
-Compare results of trained model to MVP/Phase 0 model

#### 1F. Phase 2
Document results and process in report/paper or video capture