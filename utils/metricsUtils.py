import jellyfish
import numpy as np
import pandas as pd

from statistics import mean, median
from matplotlib import pyplot as plt
from utils.pandasUtils import get_model_dt, image_column_name, save_stat_dt, save_model_dt


def replace_same_letters(word):
    same_letters = {'А': 'A', 'а': 'a',
                    'В': 'B',
                    'Е': 'E', 'е': 'e',
                    'К': 'K', 'к': 'k',
                    'М': 'M',
                    'Н': 'H',
                    'О': 'O', 'о': 'o',
                    'Р': 'P', 'р': 'p',
                    'С': 'C', 'с': 'c',
                    'Т': 'T',
                    'У': 'Y', 'у': 'y',
                    'Х': 'X', 'х': 'x',
                    'З': '3', 'з': '3',
                    '0': 'O',
                    'I': '1',
                    'l': '1',
                    }
    for oldChar, newChar in same_letters.items():
        word = word.replace(oldChar, newChar)
    return word


def get_levenstein(expected, actual):
    return jellyfish.levenshtein_distance(expected, actual)


def get_jaro(expected, actual):
    return jellyfish.jaro_similarity(expected, actual)


def get_damerau(expected, actual):
    return jellyfish.damerau_levenshtein_distance(expected, actual)


def get_hamming(expected, actual):
    return jellyfish.hamming_distance(expected, actual)


def get_match_rating_comparison(expected, actual):
    return jellyfish.match_rating_comparison(expected, actual)


def add_metric(dt, dt_model, data_name, metric, metric_name):
    dt_model[metric_name] = pd.Series(np.random.randn(len(dt_model)), index=dt_model.index)

    for image in dt_model.index:
        if image in dt.index.values:
            expected = replace_same_letters(str(dt.text.loc[image]))
            actual = dt_model[data_name].loc[image]
            actual_str = '' if actual == np.nan else replace_same_letters(str(actual))

            dt_model[image][metric_name] = metric(expected, actual_str)

    return dt_model


def add_metrics(dt, dt_model, data_name):
    add_metric(dt, dt_model, data_name, get_levenstein, 'levenstein')
    add_metric(dt, dt_model, data_name, get_jaro, 'jaro')
    add_metric(dt, dt_model, data_name, get_damerau, 'damerau')
    add_metric(dt, dt_model, data_name, get_hamming, 'hamming')
    add_metric(dt, dt_model, data_name, get_match_rating_comparison, 'rating')
    return dt_model


def stats(dt, dt_stat, dt_model, data_name):
    metrics = dt_model.columns.values
    metrics = metrics[(metrics != data_name) & (metrics != image_column_name)]
    for metric_name in metrics:
        stat(dt, dt_stat, dt_model, data_name, metric_name)


def stat(dt, dt_stat, dt_model, data_name, metric_name):
    plt.hist(dt_model[metric_name],
             bins=20,
             rwidth=0.4)
    plt.ylabel('image')
    plt.xlabel(metric_name)
    print(plt.show())

    surfaces = np.unique(dt.surface.values)
    text_types = np.unique(dt.text_type.values)

    for surface in surfaces:
        images = dt.loc[dt.surface == surface].index.values
        mask = [x in images for x in dt_model.image.values]
        values = sorted(dt_model[mask][metric_name])
        dt_stat.loc(axis=0)[data_name, metric_name, surface] = mean(values), median(values), min(values), max(values)

    for text_type in text_types:
        images = dt.loc[dt.text_type == text_type].index.values
        mask = [x in images for x in dt_model.image.values]
        values = sorted(dt_model[mask][metric_name])
        dt_stat.loc(axis=0)[data_name, metric_name, text_type] = mean(values), median(values), min(values), max(values)

    values = sorted(dt_model[metric_name])
    dt_stat.loc(axis=0)[data_name, metric_name, 'common'] = mean(values), median(values), min(values), max(values)
    save_stat_dt(dt_stat)


def get_stat(dt, dt_stat, data_name):
    dt_model = get_model_dt(data_name)
    dt_model = add_metrics(dt, dt_model, data_name)
    stats(dt, dt_stat, dt_model, data_name)
    save_model_dt(dt_model, data_name)
