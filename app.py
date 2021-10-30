from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def helloWorld():
    b = 35
    return  "<p>Hola Dios</p>"

@app.route('/pokemon', methods=['GET', 'POST', 'DELETE', 'PUT'])
def login():
    if request.method == 'GET':
        return "consultar informacion"
    elif request.method == 'POST':
        return "agregar nueva informacion bd"
    elif request.method == 'PUT':
        return "modifique informacion existente"
    elif request.method == 'DELETE':
        return "elimine informacion"
    else:
        return "template principal del login"
