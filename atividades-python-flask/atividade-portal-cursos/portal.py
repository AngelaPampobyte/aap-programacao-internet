from flask import Flask
app = Flask(__name__)
@app.route("/")
def PaginaInicial():
   return """
  <html>
  <h1>Olá! Bem vindo a Fatec Itaquaquecetuba</h1>
  <head>
  <title>Pagina Inicial Fatec Itaquaquecetuba</title>
  </head>
  <h4>Links uteis:</h4><br><br>
  <center>
  <a href="http://127.0.0.1:5000/cursos">Nossos Cursos<br><br>
  <a href="http://127.0.0.1:5000/professores">Professores<br><br>
  <a href="http://127.0.0.1:5000/disciplina/Programação para Internet">Disciplina<br><br>
  <hr>
  </center>

  </html>

 """
''
@app.route("/cursos")
def listacursos():
   return """
   <html>
   </html>

   """
@app.route("/professores")
def listaprofessores():
   return """
   <html>
   </html>

"""

@app.route("/aluno/<nome>")
def saudaraluno(nome):
   return """
 <html>
 </html>

"""

@app.route("/disciplina/<nome>")
def listadisciplinas(nome):
   return """
  <html:
  </html>

"""