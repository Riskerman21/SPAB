import pandas as pd

file_path = 'merged_data.xlsx'
data = pd.read_excel(file_path)

# Create a set of tuples containing (lat, long)
longitudes = set(zip(data['lat'], data['long']))
print(longitudes)