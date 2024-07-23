import numpy as np
import pandas as pd
#import data into panda datastructures
rain_data = pd.read_csv('raindata/raindata2023-2024.csv')
#flood_data = pd.read_excel('flooddata/')
#extract dates
rain_dates = rain_data['datetime']
import os
directory = 'flooddata/'
# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        print(file_path)

