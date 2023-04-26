from flask import Flask, render_template
from mongoengine import connect, Document, StringField, DateTimeField, ListField
connect(host='mongodb+srv://cauanjesus:87654321@cluster0.ns2mcr2.mongodb.net/test')
connect('urlDoBancoAtlas')
class Projeto(Document):
    nome_do_projeto = StringField(required=True)
    data_de_entrega = DateTimeField(required=True)
    lider = StringField(required=True)
    integrantes = ListField(StringField())


projeto = Projeto(
    nome_do_projeto='Projeto A',
    data_de_entrega='2023-12-31',
    lider='João',
    integrantes=['Maria', 'Pedro']
)
projeto.save()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
       
    return  render_template('inicial.html' , projeto)
