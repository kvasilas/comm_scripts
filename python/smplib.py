import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "vasilaskc@gmail.com"
passwd = ""

rec='kcvasilas@gmail.com'
smtp = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp, port)
server.starttls()
server.login(email, passwd)

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = rec

msg['Subject'] = "You can insert anything\n"
body = "hello Senor\n"

msg.attach(MIMEText(body, 'plain'))
sms = msg.as_string()
server.sendmail(email, sms_gateway, sms)
server.quit()
