import numpy as np
import pandas as pd
from datetime import datetime

#import data into panda datastructures
rain_data = pd.read_csv('raindata/raindata2023-2024.csv')
#flood_data = pd.read_excel('flooddata/')
print(rain_data)
#extract dates
rain_dates = rain_data['datetime']
import os

directory = 'flooddata/date/'
flooddata_dict = {}

# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        #open excel file
        file = pd.read_excel(file_path)
        #get the date of the data
        file_path = file_path.split('/')[1]
        filename = file_path.split('.')[0]
        #format date
        date_obj = datetime.strptime(filename, "%Y%m%d")
        formatted_date = date_obj.strftime("%d/%m/%Y")
        #append to date list
        flooddata_dict.update({formatted_date: file})

print(flooddata_dict)

#get dates where it rained
#for i in range(len(rain_data)):
    #check whether it rained if so add to dates rained
    #if rain_dates['precip'].iloc[i] > 0:   




