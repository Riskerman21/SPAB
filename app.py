from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from tensorflow.keras.models import load_model
import re
#pip install spacy
#python -m spacy download en_core_web_sm
import spacy
import en_core_web_sm
import pandas as pd
from dateutil import parser
from datetime import datetime

month_number_to_name = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

class process_text():

    def __init__(self):
        self.message = "Hello! I am the Thailand Flood Safety Chat Bot. I am here to provide assistance!\r\n" + \
            "Please note that I can only currently work in English, including location names.\r\n" + \
            "'You can ask me questions like where can I go?'\r\n" + \
            "'Will I be affected during a certain date in a certain district name?'\r\n"

        # Set up member variables to track user input
        self.province = None
        self.amphoe = None
        self.date = None
        self.general = None

        #Set up other variables to use NER to collect required information
        self.nlp_model = spacy.load("en_core_web_sm")
        self.nlp_model = en_core_web_sm.load()
        df = pd.read_csv('ChatBotData/province_list.csv', header=None)
        self.PROVINCES = df[0].tolist()

        df = pd.read_csv('ChatBotData/amphoe_list.csv', header=None)
        self.AMPHOES = df[0].tolist()

    def __str__(self):
        return self.message

    def question_asked(self,text):
        if 'hi' in text.lower() or 'hello' in text.lower() or 'greetings' in text.lower():
            return f"Hello! I'm the chatbot for Thailand Flood Prediction!\r\n" + "To get general advice ask about general advice.\r\n" + \
            f"To find about your area ask about your amphoe, provence and a date you would like to enquire about." 

        if 'advice' in text.lower() or 'event' in text.lower() or 'do' in text.lower():
            return f"Gather supplies, including non-perishable foods, cleaning supplies, and water for several days, in case you must leave immediately or if services are cut off in your area. Keep important documents in a waterproof container.\r\n" +\
            "If you require urgent help call 1460. You can read any extreme weather warnings via the Thai Meteorological Department (TMD) (กองพยากรณ์อากาศ) or call them on 1182."

        doc = self.nlp_model(text)

        provence_changed = False
        amphoe_changed = False
        date_changed = False


        for ent in doc.ents:
            print(ent)
            text = ent.text.replace(',', '').replace('.', '')

            if text in self.PROVINCES:
                provence_changed = True
                self.province = text

            elif f"{text} District" in self.AMPHOES:
                amphoe_changed = True
                self.amphoe = f"{text} District"

            elif ent.label_ == 'DATE':
                date_changed = True
                try:
                    date_obj = parser.parse(ent.text)
                    self.date = date_obj.month
                except:
                    self.date = datetime.now().month

        if provence_changed and amphoe_changed:
            addition = ""
            if self.date is None:
                self.date = datetime.now().month
                addition = "To enquire about a specific month please enter a date."

            prediction = predict_flood_risk(self.date, self.amphoe, self.province)
            return f"Great, Ill find that prediction for you using {self.amphoe}, {self.province} and {month_number_to_name[self.date]}.\r\n {addition}\r\n" + \
            f"The probability is {prediction}!"

        elif provence_changed or amphoe_changed:
            return f"Please enter both the provence and amphoe you would like to check was well as a date."

        else:
            return f"I'm not quite sure what you have asked of me. To get general advice ask about general advice.\r\n" + \
            "To find about your area ask about your amphoe, provence and a date you would like to enquire about."


# chatbot = process_text()
# print(chatbot.question_asked("I am in a foreign country, where do i go"))
# print(chatbot.question_asked("What is the current advice"))

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

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    email = data['email']

    send_signup_email(email)
    return jsonify({"message": "Email sent successfully"}), 200

def send_signup_email(email):
    sender_email = "abdallah33319@gmail.com"
    receiver_email = email
    password = "dkbg eznp svlw onun"

    message = EmailMessage()
    message.set_content("""Hi there,
THANK YOU for signing up!
Please reply to this email for feedback or any questions you may have.
                        """)

    message['Subject'] = "Thank You for Signing Up!"
    message['From'] = "Weather.com"
    message['To'] = receiver_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)

@app.route('/long_predict', methods=['POST'])
def long_predict():
    data = request.json
    months = int(data['month'])
    amphoe = str(data['amphoe'])
    province = str(data['province'])
    predictions = predict_flood_risk(months, amphoe, province)
    return jsonify({"predictions": predictions}), 200

@app.route('/send_to_bot', methods=['POST'])
def send_to_bot():
    user_input = request.json.get('message')
    chatbot = process_text()
    return jsonify({'answer': chatbot.question_asked(user_input)}), 200

app.run(debug=True)
