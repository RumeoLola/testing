from flask import Flask, render_template, request, flash
from form import ContactForm
from flask_mail import Mail, Message
import smtplib
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()
import os

OWN_EMAIL = os.environ.get("OWN_EMAIL")
OWN_PASSWORD = os.environ.get("OWN_PASSWORD")

print(os.environ.get("wasiuomololaz@gmail.com"))
print(os.environ.get("Deerp8rk"))

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["subject"], data["message"])
        return render_template("landing.html", msg_sent=True)
    return render_template("landing.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__=="__main__":
    app.run(debug=True)
