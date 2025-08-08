import config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do e-mail
sender = config.email
password = config.senha

def send_email(subject: str, message_body: str, recipient: str) -> None:
        
    try:
        mensagem = MIMEMultipart()
        mensagem['From'] = sender
        mensagem['To'] = recipient
        mensagem['Subject'] = subject

        corpo = message_body
        mensagem.attach(MIMEText(corpo, 'plain'))

        # Enviar o e-mail
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(sender, password)
        texto = mensagem.as_string()
        servidor.sendmail(sender, recipient, texto)
        servidor.quit()

        print(f"E-mail enviado.")
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        raise