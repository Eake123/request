import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from downloadFile import *

class Send:
    def __init__(self,
    send_from,
    send_to,
    subject,
    text,
    file,
    username,
    password):

        self.send_from = send_from
        self.send_to = send_to
        self.subject = subject
        self.text = text
        self.file = file
        self.username = username
        self.password = password
    
    def sendAttach(self):
        msg = MIMEMultipart()
        msg['From'] = self.send_from
        msg['To'] = self.send_to
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.text))

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(self.file, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=%s' %(self.file))
        msg.attach(part)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
            server=smtplib.SMTP_SSL('smtp.gmail.com',465)
            server.login(self.username,self.password)
            server.send_message(msg)


def send_attachment(fileName, url,send_from,send_to,subject,text,username,password):
    H = html(url)
    H.download(fileName)
    S = Send(send_from, send_to, subject, text, fileName, username,password)
    S.sendAttach()

