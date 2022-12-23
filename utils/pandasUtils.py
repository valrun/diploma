import numpy as np
import pandas as pd

from utils.utils import get_image_filepaths, get_name_by_path

image_column_name = 'image'
surface_column_name = 'surface'
text_type_column_name = 'text_type'
result_column_name = 'result'
csv_path = 'data/dt.csv'


def init_main_dt():
    array_ = np.empty([0, 3])
    for filename in get_image_filepaths():
        image = get_name_by_path(filename)
        array_ = np.append(array_, [[image, image.split("-")[0], '']], axis=0)

    dt = pd.DataFrame(array_[:, 1:3],
                      columns=[surface_column_name, text_type_column_name],
                      index=array_[:, 0])
    dt.index.name = image_column_name

    return dt


def init_dt(dt, data_name):
    return pd.DataFrame(columns=[data_name],
                        index=dt.index)


def get_main_dt():
    return pd.read_csv(csv_path, index_col=image_column_name)


def get_dt(data_name):
    return pd.read_csv('data/' + data_name + '.csv', index_col=image_column_name)


def save_main_dt(dt):
    dt.to_csv(csv_path)


def save_dt(dt, data_name):
    dt.to_csv('data/' + data_name + '.csv')


def fill_surface(dt):
    dt[surface_column_name] = dt[image_column_name].apply(lambda x: x.split("-")[0])
