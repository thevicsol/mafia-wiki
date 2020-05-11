from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class AddSong(FlaskForm):
    title = StringField('Название песни', validators=[DataRequired()])
    fulltitle = StringField('Полное название песни', 
                            validators=[DataRequired()])
    author = StringField('Исполнитель', validators=[DataRequired()])
    album = StringField('Альбом', validators=[DataRequired()])
    year = StringField('Год выпуска', validators=[DataRequired()])
    period = StringField('Период популярности', validators=[DataRequired()])
    history = StringField('История песни', validators=[DataRequired()])
    connected = StringField('Мемы и группы, связанные с песней', 
                            validators=[DataRequired()])

    submit = SubmitField('Отправить')