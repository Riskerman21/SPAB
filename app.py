from flask import Flask, request, jsonify
from send_email import send_signup_email

app = Flask(__name__)

@app.route("/send_email", methods=["POST"])
def send_email_handler():
    data = request.get_json()
    email = data.get("email")
    if email:
        send_signup_email(email)
        return jsonify({"message": "Email sent successfully"}), 200
    else:
        return jsonify({"error": "Email is required"}), 400

if __name__ == "__main__":
    app.run(debug=True)