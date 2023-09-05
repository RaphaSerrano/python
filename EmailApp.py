import smtplib
import email.message

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from email import encoders
def enviar_email():  
    corpo_email = """
    <p>Ola Raphael</p>
    <p>Segue email</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Envio de email"
    msg['From'] = 'raphaelserrano.2a@gmail.com'
    msg['To'] = 'raphaelserrano.2a@gmail.com'
    password = 'wgtcyvgnzndydcby' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    cam_arquivo = "D:\ProgramasEmPython\smtplib.py"
    attchment = open(cam_arquivo,'rb')

    att = email.mime.base.MIMEBase('application','octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)

    att.add_header('Content-Disposition', f'attachment; filename=smtplib.py')
    attchment.close()
    msg.attach(att)


    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Credenciais para enviar o email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')





enviar_email()