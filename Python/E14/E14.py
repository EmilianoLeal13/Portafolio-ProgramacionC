import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import getpass


sender_email = input("Ingresa el e-mail desde el que se enviara: ")
password = getpass.getpass(prompt='Password: ', stream=None)
receiver_email = input("Ingresa el e-mail que lo recibira: ")
Subject = input("Ingresa el asunto: ")
Body = input("Ingresa el cuerpo del correo: ")

message = MIMEMultipart("alternative")
message["Subject"] = Subject
message["From"] = sender_email
message["To"] = receiver_email

part1 = MIMEText(Body, "plain")
message.attach(part1)

imgPath = input("Ingresa la ruta del mensaje: ")
imageData = MIMEImage(open(imgPath, 'rb').read())
imageData.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
message.attach(imageData)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )