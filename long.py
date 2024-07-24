from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import pandas as pd 
import tensorflow as tf
import matplotlib.pyplot as plt

data = '/Users/pritikaguglani/Desktop/monthly_flood_risk_area.csv'
df = pd.read_csv(data)

print(df.head())

label_encoder = LabelEncoder()

risk_mapping = {'Low Risk': 0, 'Moderate Risk': 1, 'High Risk': 2}

df['RISK_encoded'] = df['RISK'].map(risk_mapping)
print("Risk encoding mapping:", risk_mapping)
print(df[['RISK', 'RISK_encoded']].drop_duplicates())

#Encoding RISK
encoder = OneHotEncoder()

categorical_columns = ['AMPHOE_E', 'PROV_E', 'CRITERIA'] 
encoded_data = encoder.fit_transform(df[categorical_columns])

encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(categorical_columns))

final_df = pd.concat([df[['Month']], encoded_df, df['RISK_encoded']], axis=1)

#Splitting the datasets into X and Y 
X_train, X_test, y_train, y_test = train_test_split(final_df.drop('RISK_encoded', axis=1), final_df['RISK_encoded'], test_size=0.20, random_state=42)

print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

#Normalising features 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax') 
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  
              metrics=['accuracy'])

history = model.fit(X_train_scaled, y_train,
                    epochs=50,
                    batch_size=32,
                    validation_split=0.2)

model.save('flood_risk_prediction_model.h5')

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

results = model.evaluate(X_test_scaled, y_test)
print(f"Test Loss, Test Accuracy: {results}")