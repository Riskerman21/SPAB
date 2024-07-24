import pandas as pd

file_path = 'merged_data.xlsx'
data = pd.read_excel(file_path)

# Create a set of tuples containing (lat, long)
longitudes = set(zip(data['lat'], data['long']))

# Convert the set to a list
longitude_list = list(longitudes)

# Create a DataFrame from the list
longitude_df = pd.DataFrame(longitude_list, columns=['lat', 'long'])

# Save the DataFrame to an Excel file
output_file_path = 'unique_longitudes.xlsx'
longitude_df.to_excel(output_file_path, index=False)

print(f"Data has been saved to {output_file_path}")