from flask import Flask, request, jsonify
import smtplib

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    email = data.get('email')
    contact = data.get('contact')
    selection = data.get('selection')

    send_email_notification(email, contact, selection)
    return jsonify({"message": "Details submitted successfully"}), 200

def send_email_notification(email, contact, selection):
    sender_email = "your-email@gmail.com"
    receiver_email = "Yusufshaikh7008@gmail.com"
    password = "your-email-password"
    subject = f"New Submission for {selection}"
    body = f"Email: {email}\nContact: {contact}\nSelection: {selection}"

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
    app.run(debug=True)
