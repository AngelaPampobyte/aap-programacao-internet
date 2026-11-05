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

@app.route("/bomdia")
def pagina():
    return """
   <html>
    <head><title>primeira página</title>

     <body>
       <h1>Bom dia!!!</h1>
       <hr>
       <h4>Bem vindo ao meu site</h4>

        <form>

        <h4>Esta satisfeito?</h4><br><br>

        <input type="radio" id="rdbopcao" value="sim">Sim<br><br>
        <input type="radio" id="rdbopcao" value="nao">Nao<br><br>
        </form>

        <a href="http://127.0.0.1:5000/Sobre">Clique aqui


     </body>
   <html>

    """