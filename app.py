from flask import Flask
app = Flask(__name__)
@app.route("/")
def inicio():
    return "Minha primeira aplicação web com Python"

@app.route("/Sobre")
def sobre():
    return "Sistema desenvolvido com Python e Flask"

@app.route("/contato")
def contato():
    return "Entre em contato conosto!"