import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Hero(SqlAlchemyBase):
    __tablename__ = 'hero'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    fullname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_real = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    race = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    period = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    biography = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    connected = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    write_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    writer = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

    def __repr__(self):
        return f'{self.title}'