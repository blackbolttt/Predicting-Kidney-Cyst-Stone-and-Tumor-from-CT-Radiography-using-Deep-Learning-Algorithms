import os
import shutil
import random

# Define the paths to your image dataset folders
image_dataset_path = r"G:\498R\498_Dataset\Train\Tumor"

# Define the paths to your validation image dataset folders
val_image_dataset_path = r"G:\498R\498_Dataset\Test\Tumor"

# Define the split ratio (in this case, 20% for validation)
split_ratio = 0.20

# Create the validation dataset folders if they don't exist
if not os.path.exists(val_image_dataset_path):
    os.makedirs(val_image_dataset_path)


# List all the image and label files in the dataset folders
image_files = os.listdir(image_dataset_path)


# Ensure the lists are sorted to match image files with corresponding labels
image_files.sort()


# Calculate the number of files to move to the validation dataset
num_val_files = int(split_ratio * len(image_files))

# Randomly select the files for the validation dataset
val_image_files = random.sample(image_files, num_val_files)

# Move the selected image files to the validation dataset folder
for image_file in val_image_files:
    image_src_path = os.path.join(image_dataset_path, image_file)
    image_dest_path = os.path.join(val_image_dataset_path, image_file)
    shutil.move(image_src_path, image_dest_path)


# Create text files listing the image filenames
with open('testing_image_files.txt', 'w') as train_image_file:
    train_image_file.write('\n'.join(image_files))

with open('validation_image_files.txt', 'w') as val_image_file:
    val_image_file.write('\n'.join(val_image_files))

print(f"{num_val_files} image files and their corresponding label files moved to the validation dataset.")
