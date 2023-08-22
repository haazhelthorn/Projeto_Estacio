from flask import redirect, render_template, url_for, flash, request
from .forms import Addprofissional
from loja import db, app
from .models import Workers, Categorias


@app.route('/addworker', methods=['GET','POST'])
def addworker():

    if request.method == "POST":
        getworker = request.form.get("worker")
        worker = Workers(name=getworker)
        db.session.add(worker)
        flash(f'O profissional {getworker} foi cadastrado com sucesso!', 'success')
        db.session.commit()
        return redirect(url_for('addworker'))
    return render_template('/profissionais/addworker.html', workers='workers')



@app.route('/addcat', methods=['GET','POST'])
def addcat():

    if request.method == "POST":
        getcat = request.form.get("categoria")
        cat = Categorias(name=getcat)
        db.session.add(cat)
        flash(f'A categoria {getcat} foi cadastrado com sucesso!', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('/profissionais/addworker.html')


@app.route('/addprofissional', methods=['GET','POST'])
def addprofissional():
    
    form = Addprofissional(request.form)
    return render_template('/profissionais/addprofissional.html', title="Cadastrar profissionais", form=form)
