import numpy as np
import pandas as pd

from utils.utils import get_image_filepaths, get_name_by_path

image_column_name = 'image'
surface_column_name = 'surface'
text_type_column_name = 'text_type'
result_column_name = 'result'
csv_path = 'data/dt.csv'

csv_stat_path = 'data/dt_stat.csv'
model_column_name = 'model'
type_column_name = 'type'
mean_column_name = 'mean'
median_column_name = 'median'
min_column_name = 'min'
max_column_name = 'max'


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


def init_stat_dt():
    dt = pd.DataFrame(columns=[mean_column_name,
                               median_column_name,
                               min_column_name,
                               max_column_name])
    dt.index = pd.MultiIndex.from_frame(pd.DataFrame(columns=[model_column_name, type_column_name]))
    return dt


def init_dt(dt, data_name):
    return pd.DataFrame(columns=[data_name],
                        index=dt.index)


def get_main_dt():
    return pd.read_csv(csv_path, index_col=image_column_name)


def get_stat_dt():
    return pd.read_csv(csv_stat_path).set_index([model_column_name, type_column_name])


def get_dt(data_name):
    return pd.read_csv('data/' + data_name + '.csv', index_col=data_name)


def save_main_dt(dt):
    dt.to_csv(csv_path)


def save_stat_dt(dt):
    dt.to_csv(csv_stat_path)


def save_dt(dt, data_name):
    dt.to_csv('data/' + data_name + '.csv')


def fill_surface(dt):
    dt[surface_column_name] = dt[image_column_name].apply(lambda x: x.split("-")[0])
