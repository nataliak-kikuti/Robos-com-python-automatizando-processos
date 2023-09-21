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
msg['Subject'] = "Videos aulas gratis"

html = """ 
<html>
    <body>
        <p>
        Oi, <br>
        Como vai você? <br>
        <a href="https://www.udemy.com/"> Video aulas Gratutitas </a>
        Muitas aulas para assistir
        </p>
    </body>
</html>
"""
parte1 = MIMEText(html, "html")
msg.attach(parte1)

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
senha = 'sua_senha'
s.login(fromaddr, senha)
text = msg.as_string()

s.sendmail(fromaddr, toaddr,text)

