from flask import Flask
from routes.routes import configurar_rotas
import os

app = Flask(__name__)

# Configurando chave secreta para a aplicação (usada para sessões, CSRF, etc.)
app.config['SECRET_KEY'] = 'chave_secreta'

# Definição do caminho absoluto para a pasta de upload
upload_pasta = r'C:\Users\keila_barreto\Documents\Keila\Desenvolvimento_web\senai_dsw_app_flask\uploads'
app.config['UPLOAD_FOLDER'] = upload_pasta

# Limite de 16MB para os arquivos de upload
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

# Verificando se a pasta de upload existe, caso contrário, cria a pasta
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Configurando as rotas
configurar_rotas(app)

# Executando a aplicação Flask no modo debug
if __name__ == '__main__':
    app.run(debug=True)
