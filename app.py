from flask import Flask, render_template
from formulario import CadastroForm
from formulario import LoginForm

app=Flask(__name__)
app.config['SECRET_KEY'] = 'lsrhvanlvlqtaçcojgq'

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/batepapo")
def batepapo():
    return render_template("paginas/bate_papo.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    formulario=CadastroForm()
    if formulario.validate_on_submit():
        print (formulario.email.date)
        print (formulario.name.date)
        print (formulario.senha.date)
        print (formulario.confirme.date)

    return render_template("paginas/cadastro.html", form=formulario)

@app.route("/login", methods=["GET", "POST"])
def login():
    formulario=LoginForm()
    if formulario.validate_on_submit():
        print (formulario.usuario.date)
        print (formulario.senha.date)
    return render_template("paginas/login.html",  form=formulario)

if __name__=="__main__":
    app.run(debug=True)