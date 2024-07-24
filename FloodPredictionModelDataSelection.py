import numpy as np
import pandas as pd
from datetime import datetime
import os

directory = 'flooddata/date/'
flooddata_list = []

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        excel_file = pd.ExcelFile(file_path)
        if len(excel_file.sheet_names) > 1:
            file = pd.read_excel(file_path, sheet_name=1)
            filename_without_extension = filename.split('.')[0]

            date_obj = datetime.strptime(filename_without_extension, "%Y%m%d")
            formatted_date = date_obj.strftime("%Y-%m-%d")
            file['Date'] = formatted_date
            
            flooddata_list.append(file)

flooddata_df = pd.concat(flooddata_list, ignore_index=True)

rain_data = pd.read_csv('raindata/raindata2023-2024.csv')

# Ensure date format consistency
flooddata_df['Date'] = pd.to_datetime(flooddata_df['Date'])
rain_data['datetime'] = pd.to_datetime(rain_data['datetime'])

merged_df = flooddata_df.merge(rain_data, left_on='Date', right_on='datetime', how='left')



