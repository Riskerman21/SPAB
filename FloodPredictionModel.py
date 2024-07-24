import numpy as np
import pandas as pd
from datetime import datetime
import os

# Import rain data into pandas dataframe
rain_data = pd.read_csv('raindata/raindata2023-2024.csv')

# Extract dates from rain data
rain_dates = list(rain_data['datetime'])

# Initialize dictionary to hold flood data
directory = 'flooddata/date/'
flooddata_dict = {}

# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        # Open the Excel file to check the number of sheets
        excel_file = pd.ExcelFile(file_path)
        
        # Check if the file has at least two sheets
        if len(excel_file.sheet_names) > 1:
            # Read the second sheet
            file = pd.read_excel(file_path, sheet_name=1)
            
            # Get the date of the data
            filename_without_extension = filename.split('.')[0]
            
            # Format date
            date_obj = datetime.strptime(filename_without_extension, "%Y%m%d")
            formatted_date = date_obj.strftime("%Y-%m-%d")
            
            # Append to date list
            flooddata_dict[formatted_date] = file

flood_dates = list(flooddata_dict.keys())

# Merge rain data with flood data based on dates
for n in range(len(rain_dates)):
    rain_date = rain_dates[n]
    if rain_date in flood_dates:
        for category in rain_data.columns:
            if category != 'datetime':
                flooddata_dict[rain_date] = pd.concat([flooddata_dict[rain_date], pd.DataFrame([rain_data[category]])])
