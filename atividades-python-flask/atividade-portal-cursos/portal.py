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
  <a href="http://127.0.0.1:5000/aluno/Angela">Aluno<br><br>
  <a href="http://127.0.0.1:5000/disciplina/Programação para Internet">Disciplina<br><br>
  <hr>
  </center>

  </html>

 """
''
@app.route("/cursos")
def listacursos():
   return """
   <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cursos</title>
</head>
<body>
    <h1>Cursos oferecidos na nossa unidade</h1>
    <p>Gestão da tecnologia da informação, presencial</p>
    <p>Gestão comercial</p>
    <p>Gestão de comércio eletrônico</p>
    <p>Secretariado</p>
</body>
</html>

   """
@app.route("/professores")
def listaprofessores():
   return """
   <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professores</title>
</head>
<body>
    <h1>Nossos professores</h1>
    <p>Marcos da Silva: formado em análise e desenvolvimento de sistemas,
    <br>atua a 15 anos como professor e completou 5 anos nessa instituição</p>
    <p>Angela Pamponet: formada em letras,
    <br>atua a 10 anos como professora desde sempre na nossa unidade</p>
    <p>João Almeida: formado em matemática,
    <br>atua a 20 anos na profissão e entrou esse ano na nossa unidade</p>
</body>
</html>

"""

@app.route("/aluno/<nome>")
def saudaraluno(nome):
   return f"Olá {nome} seja muito bem vindo ao nosso portal."
   """
   <html>
   <h1>teste</h1>
   <html>

   """


@app.route("/disciplina/<nome>")
def listadisciplinas(nome):
   return """
  <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Disciplina</title>
</head>
<body>
    <h1>Conheça a disciplina de programação para internet</h1>
    <p>Programação para Internet é a disciplina que capacita o aluno no desenvolvimento
    <br>de sites e aplicações web, englobando desde a interface visual até a lógica de servidores.
<br>• Foco principal: Criação de sistemas acessíveis via navegadores.
<br>• Tecnologias de interface (Front-end): HTML, CSS e JavaScript.
<br>• Tecnologias de servidor (Back-end): Linguagens de programação (como PHP, Python ou Node.js) e integração com bancos de dados.
<br>• Requisitos abordados: Design responsivo (para celulares e computadores), segurança e funcionamento do protocolo HTTP.
</p>
</body>
</html>

"""