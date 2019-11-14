from flask import Flask, render_template

app=Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/batepapo")
def batepapo():
    return render_template("paginas/bate_papo.html")

@app.route("/cadastro")
def cadastro():
    return render_template("paginas/cadastro.html")

@app.route("/login")
def login():
    return render_template("paginas/login.html")

if __name__=="__main__":
    app.run(debug=True)