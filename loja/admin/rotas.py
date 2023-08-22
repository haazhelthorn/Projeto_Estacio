from flask import render_template, session, request, redirect, url_for, flash

from loja import app, db, bcrypt
from .formulario import RegistrationForm, LoginFormulario
from .models import User


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Faça seu login', 'danger')
        return redirect(url_for('login'))

    return render_template ('admin/index.html', title='Pagina Administrativa')


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(nome=form.nome.data,
                    username=form.username.data, 
                    email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Obrigado {form.nome.data} por registrar','success')

        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Pagina de registros")


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginFormulario(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'{form.email.data} seja bem vindo!','success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash(f'Não foi possível logar no sistema', 'danger')

    return render_template ('admin/login.html',form=form, title='Pagina login')

    