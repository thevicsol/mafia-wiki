from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user

from data import db_session
from data.newmeme import AddMeme
from data.login_form import LoginForm
from data.users import User
from data.meme import Meme
from data.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/wiki.sqlite")

    @login_manager.user_loader
    def load_user(user_id):
        session = db_session.create_session()
        return session.query(User).get(user_id)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            session = db_session.create_session()
            user = session.query(User).filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect("/")
            return render_template('login.html', message="Неправильный логин или пароль", form=form)
        return render_template('login.html', title='Вход', form=form)

    @app.route("/")
    def index():
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        users = session.query(User).all()
        names = {name.id: (name.surname, name.name) for name in users}
        return render_template("index.html", jobs=jobs, names=names, title='Work log')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect("/")

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('register.html', title='Регистрация', form=form,
                                       message="Вы ввели два разных пароля")
            session = db_session.create_session()
            if session.query(User).filter(User.email == form.email.data).first():
                return render_template('register.html', title='Регистрация', form=form,
                                       message="На эту почту уже зарегистрирован участник")
            user = User(
                name=form.name.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            session.add(user)
            session.commit()
            return redirect('/login')
        return render_template('register.html', title='Регистрация', form=form)
    
    @app.route("/profile")
    def profile():
        if current_user.is_authenticated:
            mail = 'Электронная почта:' + current_user.email
            return render_template("profile.html", username=current_user.name, info=mail, title='Профиль')               
        return redirect('/register')
    
    @app.route('/addmeme', methods=['GET', 'POST'])
    def addmeme():
        add_form = AddMeme()
        if add_form.validate_on_submit():
            session = db_session.create_session()
            meme = Meme(
                title=add_form.title.data,
                date=add_form.date.data,
                author=add_form.author.data,
                people=add_form.people.data,
                period=add_form.period.data,
                status=add_form.status.data,
                about=add_form.about.data,
                history=add_form.history.data,
                connected=add_form.connected.data
            )
            session.add(meme)
            session.commit()
            return redirect('/')
        return render_template('newmeme.html', 
                               title='Новая статья про мем', form=add_form)    
    
    @app.route('/addgroup', methods=['GET', 'POST'])
    def addgroup():
        add_form = AddGroup()
        if add_form.validate_on_submit():
            session = db_session.create_session()
            group = Meme(
                title=add_form.title.data,
                date=add_form.date.data,
                author=add_form.author.data,
                people=add_form.people.data,
                period=add_form.period.data,
                status=add_form.status.data,
                about=add_form.about.data,
                history=add_form.history.data,
                connected=add_form.connected.data
            )
            session.add(group)
            session.commit()
            return redirect('/')
        return render_template('newgroup.html', 
                               title='Новая статья про группу', form=add_form)    
    
    @app.route('/addhero', methods=['GET', 'POST'])
    def addhero():
        add_form = AddHero()
        if add_form.validate_on_submit():
            session = db_session.create_session()
            hero = Hero(
                title=add_form.title.data,
                fullname=add_form.fullname.data,
                is_real=add_form.is_real.data,
                race=add_form.race.data,
                period=add_form.period.data,
                biography=add_form.biography.data,
                connected=add_form.connected.data
            )
            session.add(hero)
            session.commit()
            return redirect('/')
        return render_template('newhero.html', 
                               title='Новая статья про персонажа', 
                               form=add_form)    
    
    @app.route('/addsong', methods=['GET', 'POST'])
    def addsong():
        add_form = AddSong()
        if add_form.validate_on_submit():
            session = db_session.create_session()
            song = Song(
                title=add_form.title.data,
                fulltitle=add_form.fulltitle.data,
                author=add_form.author.data,
                album=add_form.album.data,
                year=add_form.year.data,
                period=add_form.period.data,
                history=add_form.history.data,
                connected=add_form.connected.data
            )
            session.add(song)
            session.commit()
            return redirect('/')
        return render_template('newsong.html', 
                               title='Новая статья про песню', 
                               form=add_form)      

    app.run()


if __name__ == '__main__':
    main()