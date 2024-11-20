from flask import render_template, request, redirect, url_for

def configurar_rotas(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/salute')
    def salute():
        usuario = {'nome': 'Godofredo'}
        return render_template('salute.html', usuario = usuario)

    @app.route('/form', methods=['GET', 'POST'])
    def form():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            idade = request.form['idade']
            mensagem = request.form['mensagem']
            
            print(f"Nome: {nome}, E-mail: {email}, Idade: {idade}, Mensagem: {mensagem}")
            
            return redirect(url_for('index'))
        
        return render_template('form.html')