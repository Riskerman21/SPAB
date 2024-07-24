import smtplib
from email.message import EmailMessage

def send_signup_email(email):
    # Replace these values with your own email credentials
    sender_email = "abdallah33319@gmail.com"
    receiver_email = email
    password = "dkbg eznp svlw onun"

    # Create an email message
    message = EmailMessage()
    message.set_content("Thank you for signing up! Please visit our website to complete the registration process.")

    message['Subject'] = "Thank You for Signing Up!"
    message['From'] = "Weather.com"
    message['To'] = receiver_email

    # Connect to the email server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
