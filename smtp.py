import smtplib
from email.mime.text import MIMEText
# from email.header import Header


email_de_envio = "trabalhoredes2fabio@gmail.com"
email_recebimento = "trabalhoredes2fabio@gmail.com"
senha = input(str("Senha: "))
menssagem = "Busquem conhecimento by ÉT Biluçu"
m = MIMEText(menssagem, 'plain', 'utf-8') #converte para utf-8 para ser possivel enviar email


server = smtplib.SMTP ("smtp.gmail.com", 587)
server.starttls()
server.login(email_de_envio, senha)
print("Sucesso!")
server.sendmail(email_de_envio, email_recebimento, m.as_string())
print("Email enviado para:", email_recebimento)