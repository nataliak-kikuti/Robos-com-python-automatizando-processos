import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = 'seu_email'
toaddr = 'destinatario_do_email'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Email de teste"

body = "Email enviado do nosso robo."

msg.attach(MIMEText(body, 'plain'))

filename = "panfleto.pdf"
anexo = open('panfleto.pdf', 'rb')

p = MIMEBase('application', 'octet-stream')

p.set_payload((anexo).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition','attachment; filename %s' % filename)
msg.attach(p)


s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
senha = 'sua_senha'
s.login(fromaddr, senha)
text = msg.as_string()

s.sendmail(fromaddr, toaddr,text)

