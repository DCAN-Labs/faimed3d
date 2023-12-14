import pandas as pd
import os


def add_filter_column():
    data_dir = '/home/miran045/reine097/projects/loes-scoring-2/data/filtered'
    df = pd.read_csv(os.path.join(data_dir, 'ashish_all.csv'))
    df['masks'] = df.apply(lambda row: get_mask_file_path(row['file']), axis=1)
    df.to_csv(os.path.join(data_dir, 'ashish_all_filters.csv'))


def get_mask_file_path(file_path):
    masks_dir = '/home/feczk001/shared/projects/S1067_Loes/data/MNI-space_Loes_data/masks/'
    base_name = os.path.basename(file_path)
    mask_file_path = os.path.join(masks_dir, base_name)

    return mask_file_path


if __name__ == '__main__':
    add_filter_column()
