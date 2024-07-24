import pandas as pd

df = pd.read_excel('merged_data.xlsx')

features = df[["lat", "long", "tempmax", "tempmin", "temp", "sealevelpressure", "precipprob", "humidity"]]
target_variable = df["precipcover"]

