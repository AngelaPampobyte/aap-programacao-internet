from flask import Flask
app = Flask(__name__)
@app.route("/")
def PaginaInicial():
   return """
  <html>

  </html>

 """
''
@app.route(/cursos")