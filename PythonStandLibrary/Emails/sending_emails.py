import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from email.mime.image import MIMEImage


message = MIMEMultipart()
message["from"] = "Emory.Du"
message["to"] = "orangeduxiaocheng@gmai.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("test.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("orangeduxiaocheng@gmail.com", "secret")
    smtp.send_message(message)
    print("Sent...")
