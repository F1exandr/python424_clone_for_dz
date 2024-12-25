from flask import Blueprint, render_template
from flask_login import current_user, login_user, logout_user

from app.models import Tovar
from app.main import korzina
from app.beautifulsoup.vremya_curs import cursval, clock

home_bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@home_bp.route('/')
def hors():
    cloc = clock()
    curs = cursval()
    return render_template('home/index.html', cloc=cloc, curs=curs)
@home_bp.route('/index')
def index():
    korzin = korzina()
    tovar = Tovar.query.all()
    kolvo = len(korzin)

    return render_template('home/index.html', tovars=tovar, korzina=kolvo)
