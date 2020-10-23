# This Python code is for Python version   : 2.7.12 
import os 
import numpy as np

# Root folder is the directory that contains the folder with all data
# the image data must be in a directory with subdirectories that
# represent a class label with images pertaining to the class label

# root directory with subdirectory containing data_set_folder
root_dir_path = "."
data_set_dir = "Images"

# test set folder that will be created
test_set_dir = "Test_Images"

def get_files(path=".") -> list:
    try: 
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    except: 
        print("\nError, once check the path")
        return

def get_subdirs(path=".") -> list:
    try: 
        return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    except: 
        print("\nError, once check the path")
        return

def create_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except:
        print("Directory already created")

def move_file(old_path:str, new_path:str, file_name:str):
    os.rename(os.path.join(old_path, file_name), os.path.join(new_path, file_name))

def selected_for_testing(rand_num, testing_percentage=0.75):
    return True if rand_num > testing_percentage else False




def create_test_set(label_dirs=[], dir_path="."):
    """
    Given an array of classification label directories
    Split the data in the label directories into test and training data

    Result: test_set_dir is created with sub-dir's for each label and is populated
    with a percentage of testing data based on the defined test data split size
    """
    create_dir(os.path.join(dir_path, test_set_dir))

    # for every directory
    dataset_path = os.path.join(dir_path, data_set_dir)
    testing_set_path = os.path.join(dir_path, test_set_dir)
    for label in label_dirs:
        data_label_path = os.path.join(dataset_path, label)
        testing_label_path = os.path.join(testing_set_path, label)

        # make directory for test images
        create_dir(testing_label_path)

        # get all files from sub directory from images and generate sampling values
        label_images = get_files(data_label_path)
        samplings = np.random.random_sample((len(label_images),))
        for image_filename, rand_val in zip(label_images, samplings):
            if selected_for_testing(rand_val):
                move_file(data_label_path, testing_label_path, image_filename)

def split_data_set(path="."):
    # get all class label directories from data set
    class_label_dirs = get_subdirs(os.path.join(path, data_set_dir))    
    create_test_set(class_label_dirs, path)

  
# main to split dataset
if __name__ == "__main__":
    split_data_set(root_dir_path)