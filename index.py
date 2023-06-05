import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.parse import parse_qs

from flask import Flask, jsonify, request

app = Flask(__name__)

def sender_email(objeto): 
    try:
        jsObj = json.loads(objeto)
        destine_mail = jsObj["destine_mail"][0]
        Titulo = jsObj["title"][0] 
        Message = jsObj["msg"][0] 

        # Credenciais do remetente
        # email_sender = 
        # senha_sender = 
        # email_destino = "michel.oliveira.c0@gmail.com"

        email_sender = "contato@assertivacertificado.com.br"
        senha_sender = "xvfdsgbiqwwoadpj"
        email_destino = destine_mail

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
        smtp_server.sendmail(email_sender, email_destino, mensagem.as_string())

        # Encerramento da conexão SMTP
        smtp_server.quit()
        return "E-mail enviado"
    
    except Exception as e:
        return str(e)

@app.route("/send_email", methods=['POST'])
def send_mail():
    objeto = request.get_data().decode('utf-8')
    objeto = parse_qs(objeto)
    objeto = json.dumps(objeto)

    try:
        result = sender_email(objeto)
        if result == "E-mail enviado":
            response = {"success": True, "message": "E-mail enviado com sucesso", "resultado": result}
        else:
            response = {"success": False, "message": result, "resultado": result}
    except Exception as e:
        response = {"success": False, "message": "Erro ao converter os dados."}

    return json.dumps(response)

@app.route("/")
def Hello():
    return "<p>API para encaminhar email1</p>"