from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class AddGroup(FlaskForm):
    title = StringField('Название группы', validators=[DataRequired()])
    date = StringField('Дата создания', validators=[DataRequired()])
    author = StringField('Автор группы', validators=[DataRequired()])
    people = StringField('Участвующие лица', validators=[DataRequired()])
    period = StringField('Период популярности', validators=[DataRequired()])
    status = StringField('Статус', validators=[DataRequired()])
    about = StringField('Суть группы', validators=[DataRequired()])
    history = StringField('История группы', validators=[DataRequired()])
    connected = StringField('Группы, связанные с данной', validators=[DataRequired()])

    submit = SubmitField('Отправить')
