from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

    bodyTrail = """\
        <html>
            <head></head>
            <body>
                <h1>%s</h1>
                <h3>Regards</h3>
                <h4>Aadesh Agarwal</h4>
                <p>MEng Student at Virginia Tech<br>
                Computer Science<br>
                Fall 2023<br>
                <a href="https://www.linkedin.com/in/aadesh-agarwal/">LinkedIn</a><br>
                <a href="https://github.com/aadesh-agarwal8888">GitHub</a>
                </p>
            </body>
        </html>
        """ % (body.capitalize())

    message = MIMEMultipart("alternative")
    message['From'] = "Future Intern - Task Complete"
    message['To'] = to
    message['Subject'] = subject.capitalize()
    message.attach(MIMEText(body, 'plain'))
    message.attach(MIMEText(bodyTrail, 'html'))

    server.login(server_username, server_password)

    server.sendmail(server_username, to, message.as_string())

    return "Please Check your Inbox"

if __name__ == '__main__':
    app.run()