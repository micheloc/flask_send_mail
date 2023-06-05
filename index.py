import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import Flask, jsonify, request

app = Flask(__name__)

def sender_email(objeto): 
    try:
        jsObj = json.loads(objeto)
        # email = jsObj["mail_sender"] 


        return jsObj 

        # senha = jsObj["password"] 
        # destine_mail = jsObj["destine_mail"] 

        # Titulo = jsObj["title"] 
        # Message = jsObj["msg"] 

        # # Credenciais do remetente
        # # email_sender = "contato@assertivacertificado"
        # # senha_sender = "@Ab010203"
        # # email_destino = "michel.oliveira.c0@gmail.com"

        # email_sender = email
        # senha_sender = senha
        # email_destino = destine_mail

        # # cloudflare senha : jtljxhreslzxyrhd1@
        # # Configuração da mensagem

        # mensagem = MIMEMultipart()
        # mensagem["From"] = email_sender
        # mensagem["To"] = email_destino
        # mensagem["Subject"] = Titulo
        # mensagem.attach(MIMEText(Message, "html"))

        # mensagem["Importance"] = "High"

        # # Conexão com o servidor SMTP
        # smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        # smtp_server.starttls()

        # # Autenticação no servidor SMTP
        # smtp_server.login(email_sender, senha_sender)

        # # Envio da mensagem
        # smtp_server.sendmail(email_sender, email_destino, mensagem.as_string())

        # # Encerramento da conexão SMTP
        # smtp_server.quit()
        # return "E-mail enviado"
    
    except Exception as e:
        return str(e)

@app.route("/send_email", methods=['POST'])
def send_mail():
    objeto = request.get_data().decode('utf-8')
    # try:
    #     result = sender_email(objeto)
    #     if result == "E-mail enviado":
    #         response = {"success": True, "message": "E-mail enviado com sucesso", "resultado": result}
    #     else:
    #         response = {"success": False, "message": result, "resultado": result}
    # except Exception as e:
    response = {"success": False, "message": objeto}
    return json.dumps(response)


@app.route("/")
def Hello():
    return "<p>API para encaminhar email1</p>"