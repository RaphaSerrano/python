import smtplib
import email.message


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

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Credenciais para enviar o email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')





enviar_email()