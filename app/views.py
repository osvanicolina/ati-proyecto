from flask import render_template
from app import app

@app.route('/')
def home():
   return "hello world!"

@app.route('/template')
def index():
    return render_template('index.html')

@app.route('/indexuser')
def indexuser():
    return render_template('indexuser.html')

@app.route('/inicio')
def inicio():
    return render_template('inicioprueba.html')

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

@app.route('/prueba2')
def prueba2():
    return render_template('prueba2.html')

@app.route('/reprobado')
def reprobado():
    return render_template('reprobado.html')
