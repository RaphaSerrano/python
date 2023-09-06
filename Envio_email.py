import smtplib
import email.message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def enviar_email():
    corpo_email = """
    <p>Ola Raphael</p>
    <p>Segue email</p>
    """

    msg = MIMEMultipart()
    msg['Subject'] = "Envio de email com anexo"
    msg['From'] = 'raphaelserrano.2a@gmail.com'
    msg['To'] = 'raphaelserrano.2a@gmail.com'
    password = 'wgtcyvgnzndydcby'

    # Corpo do e-mail
    msg.attach(MIMEText(corpo_email, 'html'))

    # Caminho do arquivo que você deseja anexar
    caminho_arquivo = 'D:\ProgramasEmPython\Agtech_Script.txt'

    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(arquivo.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{caminho_arquivo}"')
            msg.attach(part)
    except FileNotFoundError:
        print(f"O arquivo '{caminho_arquivo}' não foi encontrado e não será anexado ao e-mail.")

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    try:
        # Credenciais para enviar o e-mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        print('Email enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {str(e)}')
    finally:
        s.quit()

enviar_email()
