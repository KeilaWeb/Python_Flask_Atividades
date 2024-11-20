from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): # function view
    usuario = {'nome': 'Amy', 'idade': 10}
    itens = ['Maçãs', 'Peras', 'Uvas']
    
    contexto = {
        'usuario': usuario,
        'itens': itens,
        'esta_logado': True,
        'dado': {'nome': 'Flask', 'versao': '2.0'}
    }
    
    return render_template('index.html', **contexto)

@app.route('/detalhes')
def detalhes():
    usuario = {'nome': 'Godofredo', 'idade': 25}
    return render_template('detalhes.html', usuario = usuario)

if __name__ == '__main__':
    app.run(debug = True, port = 4000)