import pandas as pd
import numpy as np
import tensorflow as tf
from DataScraping import main
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from VisualiseCoordinates import visualise

if __name__ == "__main__":
    # Update the most recent forecast 
    main()

    # Get the required data
    coordinates = pd.read_excel('unique_coordinates.xlsx').dropna()
    weather_forecast = pd.read_excel('ForecastedWeather.xlsx')

    # Combine them to get each daily combination
    coordinates['key'] = 1
    weather_forecast['key'] = 1
    combined_df = pd.merge(weather_forecast, coordinates, on='key').drop('key', axis=1)
    combined_df = combined_df[["lat", "long", "tempmax", "tempmin", "temp", "sealevelpressure", "precipprob", "humidity"]]

    # Scale according to the new scraped format (since the data isn't from the same source this made predictions more reliable)
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(combined_df)
    scaled_df = pd.DataFrame(scaled_features, columns=combined_df.columns)

    # Get each day separated into its own df 
    splits = [scaled_df.iloc[i * len(coordinates):(i + 1) * len(coordinates)] for i in range(len(weather_forecast))]

    # Load the prediction model
    model = tf.keras.models.load_model('precib_cover_predicition.keras')

    predictions = []
    for split_df in splits:
        preds = model.predict(split_df)
        predictions.append(preds)

    all_preds = np.concatenate(predictions)
    result_df = pd.DataFrame({
    'lat': combined_df['lat'],
    'long': combined_df['long'],
    'pred': all_preds.flatten()  
    })

    result_df['pred'] = np.log1p(result_df['pred'])
    result_df['pred'] = result_df['pred'] - min(result_df['pred'])

    splits = [result_df.iloc[i * len(coordinates):(i + 1) * len(coordinates)] for i in range(len(weather_forecast))]
    for i, split in enumerate(splits):
        visualise(split, 3, i, 0.0006)
    

    