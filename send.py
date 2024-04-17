import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    context = ssl.create_default_context()
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls(context=context)
        server.login('yassine.tamam3@gmail.com', 'zpff ugdz odhy lcdv')

        message = MIMEMultipart("alternative")
        message["Subject"] = "HELLO????"
        message["From"] = 'yassine.tamam3@gmail.com'
        message["To"] = 'fady.sarwat377@gmail.com'
        part = MIMEText("Hello, how are you?")
        message.attach(part)

        server.sendmail('yassine.tamam3@gmail.com', 'fady.sarwat377@gmail.com', message.as_string())

    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")