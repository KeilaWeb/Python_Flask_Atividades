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
            nome = request.form.get['nome']
            email = request.form.get['email']
            novo_usuario = Usuarios(nome=nome, email=email)
            db.session.add(novo_usuario)
            db.session.commit()
        usuarios = Usuarios.query.all()            
            
        # Redireciona para a página de resultado com os dados        
        return render_template('usuarios.html', usuarios=usuarios)
    
    @app.route('/result')
    def usuarios():
        nome = request.args.get('nome')
        email = request.args.get('email')
        mensagem = request.args.get('mensagem')
        return render_template('result.html', nome=nome, email=email, mensagem=mensagem)