import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('trabalhoredes2fabio@gmail.com', '4c3e5d88')
mail.list()
mail.select("inbox") # conecta ao inbox

result, data = mail.search(None, "ALL")

ids = data[0] # dados são uma lista.
id_list = ids.split() # ids é uma sequência separada por espaço
ultimo_email_id = id_list[-1] # pega o ultimo email


result, data = mail.fetch(ultimo_email_id, "(RFC822)") # busca o corpo do email (RFC822) para o ID fornecido


raw_email = data[0][1] # aqui é o corpo do email com seus headers
msg = email.message_from_bytes(raw_email)

msg2 = (msg.get_payload(None, True).decode())

print("Messagem do Email:", msg2)
#print("Mensagem vinda do Email", msg.get_payload()[1].get_payload(decode=True).decode())
