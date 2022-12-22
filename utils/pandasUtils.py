import pandas as pd

image_column_name = 'image'
surface_column_name = 'surface'
csv_path = 'data/dt.csv'


def init_dt():
    return pd.DataFrame(columns=[image_column_name, surface_column_name])


def get_dt():
    return pd.read_csv(csv_path, index_col=' ')


def save_dt(dt):
    dt.to_csv(csv_path)


def fill_surface(dt):
    dt[surface_column_name] = dt[image_column_name].apply(lambda x: x.split("-")[0])
