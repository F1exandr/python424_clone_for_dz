from flask import Blueprint, render_template
from app.models import Catalog_add, Categories, Tovar
from app.main import db

catalog_bp = Blueprint('catalog', __name__, template_folder='templates', static_folder='static')


@catalog_bp.route('/catalog')
def catalog():
    categories = Categories.query.all()
    tovars = Tovar.query.all()
    return render_template('catalog.html', categories=categories, tovars=tovars)
