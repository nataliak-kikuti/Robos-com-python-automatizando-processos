import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from corpo_email_html import corpo_email

fromaddr = 'seu_email'
toaddr = 'destinatario_do_email'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Videos aulas gratis"


parte1 = MIMEText(corpo_email, "html")
msg.attach(parte1)

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
senha = 'sua_senha'
s.login(fromaddr, senha)
text = msg.as_string()

s.sendmail(fromaddr, toaddr,text)

