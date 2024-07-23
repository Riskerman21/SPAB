import numpy as np
import pandas as pd
from datetime import datetime
import os

# Import rain data into pandas dataframe
rain_data  = pd.read_csv('raindata/raindata2023-2024.csv')
print(rain_data)

# Extract dates from rain data
rain_dates = list(rain_data['datetime'])

# Initialize dictionary to hold flood data
directory = 'flooddata/date/'
flooddata_dict = {}

# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        # Open excel file
        file = pd.read_excel(file_path)
        print(file.shape)
        
        # Get the date of the data
        filename_without_extension = filename.split('.')[0]
        
        # Format date
        date_obj = datetime.strptime(filename_without_extension, "%Y%m%d")
        formatted_date = date_obj.strftime("%d/%m/%Y")
        
        # Append to date list
        flooddata_dict[formatted_date] = file

flood_dates = list(flooddata_dict.keys())

# Merge rain data with flood data based on dates
for n in range(len(rain_dates)):
    rain_date = rain_dates[n]
    for i in range(len(flood_dates)):
        flood_date = flood_dates[i]
        if flood_date == rain_date:
            flood_data = flooddata_dict[flood_date]
            rain_data.loc[n, flood_data.columns] = flood_data.values[0]




