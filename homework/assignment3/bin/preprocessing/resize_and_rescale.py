# Rescale registered images -1 to 1 range.

import itertools
import nibabel as nib
import numpy as np
import os

# Constants for path names
OLD_TRAIN_IMG = "../../data/Train/img_registered/"
NEW_TRAIN_IMG = "../../data/Train/img_rescaled/"
OLD_VAL_IMG = "../../data/Val/img_registered/"
NEW_VAL_IMG = "../../data/Val/img_rescaled/"

# Rescale the images
# First for training set
for file_name in os.listdir(NEW_TRAIN_IMG):
    # Load the image
    image = nib.load(NEW_TRAIN_IMG + file_name)
    # Get the array of values
    image_data = image.get_fdata()
    # Set zero values to -1000, since values that are exactly zero should represent padded background
    image_data = np.where(image_data == 0.0, -1000, image_data)
    # Divide by 1000 to get in -1 to 1 range
    image_data = image_data / 1000.0
    # Save the image
    image = nib.Nifti1Image(image_data, image.affine)
    nib.save(image, NEW_TRAIN_IMG + file_name)

# Rescale the validation set
for file_name in os.listdir(NEW_VAL_IMG):
    # Load the image
    image = nib.load(NEW_VAL_IMG + file_name)
    # Get the array of values
    image_data = image.get_fdata()
    # Set zero values to -1000, since values that are exactly zero should represent padded background
    image_data = np.where(image_data == 0.0, -1000, image_data)
    # Divide by 1000 to get in -1 to 1 range
    image_data = image_data / 1000.0
    # Save the image
    image = nib.Nifti1Image(image_data, image.affine)
    nib.save(image, NEW_VAL_IMG + file_name)