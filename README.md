# Image classification Dataset splitter
Python script written to save me time from manually creating a testing set from a single directory filled with classified images. Instead of manually creating a testing set (or even worse using the same training set for testing) I wrote this script in 10 mins to help you create a testing set for your classified images. Simply create dircotry as seen below:
* Root Directory
  * Dataset_dir
    * label_1_images
    * label_2_images
    * ....
    * label_n_images
  
The script will then take all of the images for each label and create a testing set by splitting the data based on a percentage you define in the script.
## Result
* Root Directory
  * Dataset_dir
    * label_1_images
    * label_2_images
    * ....
    * label_n_images
  * testing_set_dir
    * label_1_images
    * label_2_images
    * ....
    * label_n_images

Where a percentage of the labeled images are moved to the testing set which is created for you :smile:
