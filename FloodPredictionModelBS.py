import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pickle

def split_data():
    df = pd.read_excel('merged_data.xlsx')
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    split_index = int(len(df) * 0.8)
    df_train = df.iloc[:split_index]
    df_test = df.iloc[split_index:]

    features_train = df_train[["lat", "long", "tempmax", "tempmin", "temp", "sealevelpressure", "precipprob", "humidity"]]
    target_variable_train = df_train["precipcover"]

    features_mean = features_train.mean()
    features_train = features_train.fillna(features_mean)
    
    target_mean = target_variable_train.mean()
    target_variable_train = target_variable_train.fillna(target_mean)

    scaler = StandardScaler()
    features_train_scaled = scaler.fit_transform(features_train)

    features_test = df_test[["lat", "long", "tempmax", "tempmin", "temp", "sealevelpressure", "precipprob", "humidity"]]
    target_variable_test = df_test["precipcover"]

    features_test = features_test.fillna(features_mean)
    target_variable_test = target_variable_test.fillna(target_mean)

    features_test_scaled = scaler.transform(features_test)

    return features_train_scaled, target_variable_train, features_test_scaled, target_variable_test, scaler

def model_creation(X_train_scaled):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1)  
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
                loss='mean_squared_error',
                metrics=['mae'])
    
    return model

if __name__ == '__main__':
    features_train, target_variable_train, features_test, target_variable_test, scaler = split_data()
    model = model_creation(features_train)

    history = model.fit(features_train, target_variable_train,
                        epochs=50,
                        batch_size=32,
                        validation_split=0.2)

    model.save('precib_cover_predicition.keras')

    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

    print()

    X_test_scaled = scaler.fit_transform(features_test)
    predictions = model.predict(X_test_scaled)

    mae = mean_absolute_error(target_variable_test, predictions)
    mse = mean_squared_error(target_variable_test, predictions)
    r2 = r2_score(target_variable_test, predictions)

    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")
    print(f"R² Score: {r2}")

    with open('scaler_model.pkl', 'wb') as file:
        pickle.dump(scaler, file)