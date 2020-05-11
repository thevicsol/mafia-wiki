from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField
from wtforms.validators import DataRequired


class AddHero(FlaskForm):
    title = StringField('Имя персонажа', validators=[DataRequired()])
    fullname = StringField('Полное имя', validators=[DataRequired()])
    is_real = BooleanField('Реален ли персонаж')
    race = StringField('Раса', validators=[DataRequired()])
    period = StringField('Период популярности', validators=[DataRequired()])
    biography = StringField('Биография', validators=[DataRequired()])
    connected = StringField('Мемы и группы, связанные с персонажем',
                            validators=[DataRequired()])

    submit = SubmitField('Отправить')
