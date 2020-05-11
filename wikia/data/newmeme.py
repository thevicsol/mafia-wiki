from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class AddMeme(FlaskForm):
    title = StringField('Название мема', validators=[DataRequired()])
    date = StringField('Дата создания', validators=[DataRequired()])
    author = StringField('Автор мема', validators=[DataRequired()])
    people = StringField('Участвующие лица', validators=[DataRequired()])
    period = StringField('Период популярности', validators=[DataRequired()])
    status = StringField('Статус', validators=[DataRequired()])
    about = StringField('Суть мема', validators=[DataRequired()])
    history = StringField('История мема', validators=[DataRequired()])
    connected = StringField('Мемы, связанные с данным', validators=[DataRequired()])

    submit = SubmitField('Отправить')
