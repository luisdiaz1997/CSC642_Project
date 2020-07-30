import glob
import re


def get_images(some_dir):
    return glob.glob(some_dir+'/*')


def format_data(data):
    data_list = []
    for element in data:
        element_split = re.split('[/.]', element)
        data_list.append({"name": element_split[-2], "src": "/"+element})

    return data_list
