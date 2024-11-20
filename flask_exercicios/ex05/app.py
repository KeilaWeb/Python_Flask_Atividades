from flask import Flask
from models import db
from routes.route import configurar_rotas

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Adicionei para evitar um warning

db.init_app(app)  # Inicialize o db com o app

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

with app.app_context(): 
    db.create_all()

configurar_rotas(app)

if __name__ == '__main__':
    app.run(debug=True)
