import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from tensorflow.keras.models import load_model

# Load the saved model
def predict_flood_risk(months: int, amphoe: str, province: str) -> str:
    model = load_model('./flood_risk_prediction_model.h5')

    # Load and preprocess the original data to refit encoder and scaler
    data = './monthly_flood_risk_area.csv'
    df = pd.read_csv(data)

    # Define the risk mapping used during training
    risk_mapping = {'Low Risk': 0, 'Moderate Risk': 1, 'High Risk': 2}

    # Define categorical columns used during training
    categorical_columns = ['AMPHOE_E', 'PROV_E']

    # Fit the OneHotEncoder on the original categorical data
    encoder = OneHotEncoder()
    encoder.fit(df[categorical_columns])

    # Fit the StandardScaler on the original training data
    # Combine all preprocessing steps
    df['RISK_encoded'] = df['RISK'].map(risk_mapping)
    encoded_data = encoder.transform(df[categorical_columns])
    encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(categorical_columns))
    final_df = pd.concat([df[['Month']], encoded_df, df['RISK_encoded']], axis=1)
    X_train = final_df.drop('RISK_encoded', axis=1)
    scaler = StandardScaler()
    scaler.fit(X_train)

    # Define the new data
    new_data = pd.DataFrame({
        'Month': [months],
        'AMPHOE_E': [amphoe],
        'PROV_E': [province],
    })

    # Preprocess the new data
    encoded_new_data = encoder.transform(new_data[categorical_columns])
    encoded_new_df = pd.DataFrame(encoded_new_data.toarray(), columns=encoder.get_feature_names_out(categorical_columns))
    final_new_df = pd.concat([new_data[['Month']], encoded_new_df], axis=1)
    new_data_scaled = scaler.transform(final_new_df)

    # Make predictions
    predictions = model.predict(new_data_scaled)
    predicted_classes = predictions.argmax(axis=-1)

    # Map predicted classes back to risk categories
    inverse_risk_mapping = {v: k for k, v in risk_mapping.items()}
    predicted_risk_categories = [inverse_risk_mapping[pred] for pred in predicted_classes]
    return predicted_risk_categories[0]
