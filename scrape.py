import glob
import re
import pandas as pd
import numpy as np



def get_images(some_dir):
    return glob.glob(some_dir+'/*')


def format_data(data):
    data_list = []
    for element in data:
        element_split = re.split('[/.]', element)
        data_list.append([element_split[-2], "/"+element])

    return data_list

def construct_data(some_dir, location=np.array([[34.086292, -118.216081]])):



    data = np.array(format_data(get_images(some_dir)))
    df = pd.DataFrame(data= data, columns=['name', 'im_src'])
    df['discount'] = np.random.rand(len(df), 1) > 0.5

    locations = location+ (1e-2*np.random.randn(len(df), 2))
    df['lat'] = locations[:, 0]
    df['lng'] = locations[:, 1]
    
    print(locations)
    print(df)
    return df
