import requests
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_admin import Admin
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
admin = Admin(app, name='My Admin Panel', template_mode='bootstrap4')

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
from .catalog.catalog import catalog_bp

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(error_bp)
app.register_blueprint(tovar_bp)

app.register_blueprint(catalog_bp)


@app.route('/get_course', methods=['GET'])
def get_course():
    url = 'https://api.exchangerate.host/latest?base=USD&symbols=RUB'
    try:
        response = requests.get('https://api.exchangerate.host/latest?base=USD&symbols=RUB')
        print(response.json())
        print(response.status_code)
        # print(response.)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()  # Преобразуем ответ в JSON
        # return jsonify(data)

        # Извлекаем курс доллара к рублю

        error_type = data.get('error', {}).get('type')
        succ = data.get('success')
        return {'err': error_type, 'succ': succ}
        # if usd_to_rub:
        #     return jsonify({'currency': 'USD', 'rate': usd_to_rub})
        # else:
        #     return jsonify({'error': 'Rate not found'}), 404

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=5001, debug=True)
