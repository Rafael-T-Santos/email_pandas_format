import pandas as pd
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

def enviar_email():
  df = pd.read_csv('data.csv', sep=';')

  username = 'seuemail@gmail.com'
  password = 'suasenha'

  recipients = ['destinatario_1@hotmail.com', 'destinatario_2@gmail.com'] 
  emaillist = [elem.strip().split(',') for elem in recipients]
  msg = MIMEMultipart()
  msg['Subject'] = "Assunto do e-mail"
  msg['From'] = 'seuemail@gmail.com'


  html = """\
  <html>
    <head></head>
    <body>
      {0}
    </body>
  </html>
  """.format(df.to_html(index=False))

  part1 = MIMEText(html, 'html')
  msg.attach(part1)

  try:

      server = smtplib.SMTP(host='smtp.gmail.com', port=587)
      server.starttls()
      server.login(username, password)
      server.sendmail(msg['From'], emaillist , msg.as_string())
      server.close()

  except Exception as e:
      print("Error for connection: {}".format(e))
