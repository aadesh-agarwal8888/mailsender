from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server_username = "aadeshmailtester@gmail.com"
server_password = "nowornever"

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/emails', methods=["POST"])
def get_mail():
    request_data = request.get_json()
    to = request_data["to"]
    subject = request_data["subject"]
    body = request_data["body"]

    message = MIMEText(body.capitalize())
    message['From'] = "Future Intern - Task Complete"
    message['To'] = to
    message['Subject'] = subject.capitalize()

    server.login(server_username, server_password)

    server.sendmail(server_username, to, message.as_string())

    return "Please Check your Inbox"

if __name__ == '__main__':
    app.run()