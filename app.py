from flask import Flask, render_template

app = Flask("hello")

@app.route("/")
@app.route("/hello")
def hello():
    return render_template('index.html')

@app.route("/meucontato")
def meuContato():
   return render_template('contatos.html')
