import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template


smtp = {
    'smtp_host': 'smtp.freesmtpservers.com',
    'smtp_port': 25,
    'smtp_user': 'contato@linuxdivision.com',
    'smtp_password': 'XXXXXXX'
}


def main():
    template = carregar_template()
    # Ler planilha com pandas
    planilha = pd.read_excel('planilha.xlsx')

    # Iterar pelos contatos na planilha
    for indice, contato in planilha.iterrows():
        mensagem = criar_email(contato, smtp, template)
        envier_email(contato, smtp, mensagem)

    print('E-mails enviados com sucesso!')


def carregar_template():
    # Ler o modelo HTML do arquivo
    with open('modelo.html', 'r') as f:
        modelo_html = f.read()
    template = Template(modelo_html)
    return template


def criar_email(contato, smtp, template):
    corpo_mensagem = template.render(nome=contato['nome'])
    # Configurar mensagem de e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = smtp['smtp_user']
    mensagem['To'] = contato['email']
    mensagem['Subject'] = 'Bem-vindo(a) ao nosso site!'
    mensagem.attach(MIMEText(corpo_mensagem, 'html'))
    return mensagem


def envier_email(contato, smtp, mensagem):
    servidor = smtplib.SMTP(smtp['smtp_host'], smtp['smtp_port'])
    #servidor.starttls()
    #servidor.login(smtp['smtp_user'], smtp['smtp_password'])
    servidor.sendmail(smtp['smtp_user'], contato['email'], mensagem.as_string())
    servidor.quit()


if __name__ == '__main__':
    main()
