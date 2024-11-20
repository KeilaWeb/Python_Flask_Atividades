from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        idade = request.form['idade']
        mensagem = request.form['mensagem']
        
        #Aqui você pode processar os dados do formulario,
        #como salvar em um banco de dados ou enviar  um e-mail.
        print(f"Nome: {nome}, E-mail: {email}, Idade: {idade}, Mensagem: {mensagem}")
        
        return redirect(url_for('obrigado'))
    
    return render_template('formulario.html')

@app.route('/obrigado')
def obrigado():
    return "Obrigado por enviar o formulario"

if __name__ == '__main__':
    app.run(debug = True)