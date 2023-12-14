import sys

import nibabel as nib
import os
from os import listdir
from os.path import isfile, join

from tqdm import tqdm


def create_filter_file(input_file, output_dir):
    isExist = os.path.exists(output_dir)
    if not isExist:
        os.makedirs(output_dir)
    img = nib.load(input_file)
    image_data = img.get_fdata()
    new_data = image_data.copy()
    data_shape = image_data.shape
    for i in range(data_shape[0]):
        for j in range(data_shape[1]):
            for k in range(data_shape[2]):
                if int(image_data[i][j][k]) == 0:
                    new_data[i][j][k] = 0
                else:
                    new_data[i][j][k] = 1
    mask_img = nib.Nifti1Image(new_data, img.affine, img.header)
    output_file_path = os.path.join(output_dir, os.path.basename(input_file))
    nib.save(mask_img, output_file_path)


if __name__ == '__main__':
    folder = sys.argv[1]
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    for f in tqdm(onlyfiles):
        create_filter_file(os.path.join(folder, f), sys.argv[2])
