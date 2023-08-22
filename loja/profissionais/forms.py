from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators


class Addprofissional(Form):

    name = StringField('Nome: ', [validators.DataRequired()])
    price = IntegerField('Preço: ', [validators.DataRequired()])
    discount = IntegerField('Desconto: ', [validators.DataRequired()])
    description = TextAreaField('Descrição: ', [validators.DataRequired()])
    colors = TextAreaField('Cor: ', [validators.DataRequired()])
     
    image_1 = FileField('image_1: ' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField('image_2: ' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('image_3: ' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])