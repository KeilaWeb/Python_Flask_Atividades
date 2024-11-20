from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return "Olá Galera!!"
    return render_template('index.html')

@app.route('/variaveis')
def variaveis():
    nome = "Lindofredo"
    return render_template('variaveis.html', usuario=nome)

@app.route('/listas')
def listas():
    itens = ['Item 1', '1Item 2', 'Item 3', 'Item 4']
    return render_template('listas.html', itens=itens)

@app.route('/dicionarios')
def dicionarios():
    usuario_info = {
        "nome": "Gustavo",
        "idade": 4,
        "cidade": "Jaraguá do Sul",
        "interesses": ["Desenho", "Brincar com blocos", "Jogos de tabuleiro"]
    }
    return render_template('dicionarios.html', usuario=usuario_info)

@app.route('/listas_dicionarios')
def listas_dicionarios():
    usuarios = [
        {"nome": "Gustavo", "idade": 4, "cidade": "Jaraguá do Sul" },
        {"nome": "José", "idade": 6, "cidade": "Jaraguá do Sul"}
    ]
    return render_template('listas_dicionarios.html', usuarios=usuarios)
    
@app.route('/controle_fluxo_condicionais')
def controle_fluxo_condicionais():
    usuario = {
        "nome": 'Gustavo',
        "idade": 22,
        "cidade": "Jaraguá do Sul",
        "premium": True 
    }
    return render_template('controle_fluxo_condicionais.html', usuario = usuario)

@app.route('/filtros_jinja')
def filtros_jinja():
    usuario = {
        "nome": 'Samara',
        "idade": 72,
        "cidade": "Piaui"
    }
    mensagem = "Bem-vindo ao nosso site"
    return render_template('filtros_jinja.html', usuario = usuario, mensagem = mensagem)

if __name__ == '__main__':
    app.run(debug=True)
