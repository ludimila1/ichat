from flask import Flask, render_template
site = Flask(__name__)


@site.route("/index")
def index():
    return render_template("index.html")

@site.route("/batepapo")
def batepapo():
    return render_template("paginas/bate_papo.html")


@site.route("/cadastro")
def cadastro():
    return render_template("paginas/cadastro.html")


@site.route("/login")
def login():
    return render_template("paginas/login.html")

    

if (__name__== "__main__"):
    site.run(debug=True, port=5001)







