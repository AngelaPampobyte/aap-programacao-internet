from flask import Flask
app = Flask(__name__)
@app.route("/")
def inicio():
    return "Minha primeira aplicação web com Python e Flask"

# comando para rodar: python -m flask --app app run --debug