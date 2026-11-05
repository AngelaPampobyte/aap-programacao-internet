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

@app.route("/aluno/<nome>")
def aluno(nome):
    return f"Olá, {nome}! Bem vindo a disciplina."

@app.route("/media/<float:nota1>/<float:nota2>")
def media(nota1, nota2):
    resultado = (nota1 + nota2)/2
    return f"A media do aluno é {resultado}"