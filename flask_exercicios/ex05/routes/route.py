from flask import render_template, request, redirect, url_for, flash
from ..models import db, Usuario

def configurar_rotas(app):
    @app.route('/')
    def index():
        usuarios = Usuario.query.all()  # busca por usuários
        return render_template('index.html', usuarios=usuarios)  # Passando a lista de usuários
    
    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/form', methods=['GET', 'POST'])
    def form():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            
            novo_usuario = Usuario(nome=nome, email=email)
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Usuário criado com sucesso!', 'success')
            return redirect(url_for('index'))
        
        return render_template('form.html')

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
        usuario = Usuario.query.get_or_404(id)
        if request.method == 'POST':
            usuario.nome = request.form['nome']
            usuario.email = request.form['email']
            db.session.commit()
            flash('Usuário atualizado com sucesso!', 'success')
            return redirect(url_for('index'))
        
        return render_template('edit_user.html', usuario=usuario)

    @app.route('/delete/<int:id>', methods=['POST'])
    def delete(id):
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuário excluído com sucesso!', 'success')
        return redirect(url_for('index'))
