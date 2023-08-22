from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    nome = StringField('Nome completo :', [validators.Length(min=4, max=25)])
    username = StringField('Usuário :', [validators.Length(min=4, max=25)])
    email = StringField('Email :', [validators.Length(min=6, max=35)])
    password = PasswordField('Digite sua senha: ', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senhas não são iguais')
    ])
    confirm = PasswordField('Repita a senha: ')
    accept_tds = BooleanField('Eu aceito os TDS', [validators.DataRequired()])

    
class LoginFormulario(Form):
    email = StringField('Email :', [validators.Length(min=6, max=35)])
    password = PasswordField('Digite sua senha: ', [validators.DataRequired()])