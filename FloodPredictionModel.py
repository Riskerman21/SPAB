import numpy as np
import pandas as pd

#import data into panda datastructures
rain_data = pd.read_csv('raindata/raindata2023-2024.csv')
flood_data = pd.read_excel('flooddata/')

#extract dates
rain_dates = rain_data['datetime']

#get dates where it rained
for i in range(len(rain_data)):
    #check whether it rained if so add to dates rained
    if rain_dates['precip'].iloc[i] > 0:    
        dates_rained 




