import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.main import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin




@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    password_hash = sa.Column(sa.String(255), nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)
    admin = sa.Column(sa.Boolean, default=False)

    address = db.relationship('Address', backref='address', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Address(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    city = sa.Column(sa.String(255))
    ulica = sa.Column(sa.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Catalog_add(db.Model):
    __tablename__ = 'catalogs'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    tovar_id = db.Column(db.Integer, db.ForeignKey('tovars.id'))

    category = db.relationship('Categories', back_populates='catalogs')
    tovar = db.relationship('Tovar', back_populates='catalogs')


class Categories(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(255))
    appointment = db.Column(db.String(255))
    brand = db.Column(db.String(255))

    tovars = db.relationship('Tovar', back_populates='category', lazy='dynamic')
    catalogs = db.relationship('Catalog_add', back_populates='category', lazy='dynamic')


class Tovar(db.Model):
    __tablename__ = 'tovars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    url_photo = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    ostatok = db.Column(db.Integer, default=0)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Categories', back_populates='tovars')
    catalogs = db.relationship('Catalog_add', back_populates='tovar', lazy='dynamic')