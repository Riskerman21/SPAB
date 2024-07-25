from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
from long_perdict import predict_flood_risk

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
    # Extract the necessary input data for the long predict model
    input_data = [data['months'], data['amphoe'], data['province']]  # Replace with actual input fields

    predict_flood_risk(input_data)
    # Return the predictions as a JSON response
    return jsonify({"prediction"}), 200

if __name__ == '__main__':
    app.run(debug=True)