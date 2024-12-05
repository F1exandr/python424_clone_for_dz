from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from database import Config
from flask_login import LoginManager

app = Flask(__name__, static_folder='static')
login_manager = LoginManager(app)

app.config.from_object(Config)
# Добавляем путь сохранения изображения
# Это так же можно сделать (и правильно сделать) в классе конфиг
app.config['UPLOAD_FOLDER'] = '/app/static'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from .models import User

korzina_list = []


def korzina() -> list:
    global korzina_list
    return korzina_list


with app.app_context():
    db.create_all()
    have_user = User.query.first()
    # print(have_user)
    if not have_user:
        from seed import seeds

        seeds()

from .auth.auth import auth_bp
from .home.home import home_bp
from .error.error import error_bp
from .tovar.tovar import tovar_bp

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(error_bp)
app.register_blueprint(tovar_bp)



if __name__ == '__main__':
    app.run(port=5001, debug=True)
