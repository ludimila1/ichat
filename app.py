from flask import Flask, render_template
from formulario import CadastroForm

from formulario import LoginForm
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = 'lsrhvanlvlqtaçcojgq'
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
#db.create_all()
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Text, nullable=False)
    senha = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "usuario: %r" % self.usuario

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
        u=Usuario()
        u.usuario=formulario.name.data
        u.email = formulario.email.data
        u.senha = formulario.senha.data
        db.session.add(u)
        db.sessoin.commit()

    return render_template("paginas/cadastro.html", form=formulario)

@app.route("/login", methods=["GET", "POST"])
def login():
    formulario=LoginForm()
    if formulario.validate_on_submit():
        print (formulario.usuario.data)
        print (formulario.senha.data)
    return render_template("paginas/login.html",  form=formulario)

if __name__=="__main__":
    app.run(debug=True)