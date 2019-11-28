from flask import Flask, render_template
from formulario import CadastroForm, MensagemForm

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
    #msg = db.relationship('Mensagens', backref='usario', lazy=True)


    def __repr__(self):
        return "usuario: %r" % self.usuario

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'),nullable=False)

    def __repr__(self):
        return "%r" % self.texto

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/batepapo", methods=['POST','GET'])
def batepapo():
    form = MensagemForm()
    if form.validate_on_submit():
        msg = Mensagem()
        msg.texto = form.texto.data
        msg.usuario_id = 2
        db.session.add(msg)
        db.session.commit()
    
    mensagens = Mensagem.query.all()
    return render_template("paginas/bate_papo.html", form=form, mensagens=mensagens)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    form = CadastroForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        user1 = Usuario()
        user1.usuario = form.usuario.data
        user1.email = form.email.data
        user1.senha = form.senha.data
        db.session.add(user1)
        db.session.commit()

  
    return render_template("paginas/cadastro.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    formulario=LoginForm()
    if formulario.validate_on_submit():
        print (formulario.usuario.data)
        print (formulario.senha.data)
    return render_template("paginas/login.html",  form=formulario)

if __name__=="__main__":
    app.run(debug=True, port=8888)