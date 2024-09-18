import smtplib,ssl,os,mimetypes
from email.message import EmailMessage

def mail(correo,text,subject):
  message = EmailMessage()
  message.set_content(text)
  message['Subject'] = subject
  message['From'] = "edugn2298@gmail.com"
  message['To'] = correo
  
  smtp_server = 'smtp.gmail.com'
  smtp_port = 587


  with smtplib.SMTP(smtp_server, smtp_port) as server:
      server.starttls()  # Habilitar cifrado TLS
      server.login("edugn2298@gmail.com", "xlub emjr nazy tflj")  
      server.send_message(message)