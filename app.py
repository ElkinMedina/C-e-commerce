from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/offers')
def offers():
    return render_template('offers.html')

@app.route('/registroUsuario')
def registroUsuario():
    return render_template('registroUsuario.html')

@app.route('/nuevoUsuario')
def nuevoUsuario():
    return render_template('nuevoUsuario.html')
