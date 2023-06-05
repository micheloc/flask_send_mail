import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import Flask

app = Flask(__name__)

def sender_email(objeto): 
    jsObj = json.loads(objeto)

    Titulo = jsObj["tit"] 
    Message = jsObj["msg"] 

    # # analisa os parâmetros da string de consulta em um dicionário Python
    # params = urllib.parse.parse_qs(objeto_decodificado)
    # # cria um objeto Python com os parâmetros analisados
    # jsObj = {
    #     'title': params['tit'],
    #     'message': params['msg']
    # }
    # # 
    # Titulo = jsObj["tit"] # Sua string de coordenadas
    # Message = jsObj["msg"]

    # Credenciais do remetente
    email_sender = "i9camposoftware@gmail.com"
    senha_sender = "jtljxhreslzxyrhd"


    # cloudflare senha : jtljxhreslzxyrhd1@

    # Destinatário e assunto do email
    # email_destino = "rafaela@siccerrado.com.br,roberto@siccerrado.com.br,michel.oliveira.c0@gmail.com,tiagotrance3@hotmail.com"
    email_destino = "roberto@siccerrado.com.br,tiagotrance3@hotmail.com"
    lista_destinos = email_destino.split(",")

    # Configuração da mensagem
    mensagem = MIMEMultipart()
    mensagem["From"] = email_sender
    mensagem["To"] = email_destino
    mensagem["Subject"] = Titulo
    mensagem.attach(MIMEText(Message, "html"))
    mensagem["Importance"] = "High"

    # Conexão com o servidor SMTP
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()

    # Autenticação no servidor SMTP
    smtp_server.login(email_sender, senha_sender)

    # Envio da mensagem
    smtp_server.sendmail(email_sender, lista_destinos, mensagem.as_string())

    # Encerramento da conexão SMTP
    smtp_server.quit()
    return "E-mail enviado"



@app.route("/")
def Hello():
    return "<p>Hello</p>"