from glob import glob

import cv2

image_path = '/Users/vryndina/study/d-dataset/*/*.jpg'


easyocr_column_name = 'easyocr'
paddleocr_column_name = 'paddleocr'
doctr_column_name = 'doctr'
pytesseract_column_name = 'pytesseract'


def get_image_filepaths():
    return glob(image_path)


def get_name_by_path(filename):
    return filename.split("/").pop().split(".")[0]


def get_rgb_image(filename):
    img_cv = cv2.imread(filename)
    return cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
