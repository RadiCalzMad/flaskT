from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models import test1

main = Blueprint('main', __name__)

@main.route('/')
def index():
    datas = test1.query.all()
    return render_template('index.html', datas=datas)

@main.route('/sign')
def sign():
    return render_template('sign.html')

@main.route('/sign', methods=['POST'])
def sign_post():
    name = request.form.get('name')
    email = request.form.get('email')
    number = request.form.get('number')

    new_data = test1(name=name, email=email, number=number)
    db.session.add(new_data)
    db.session.commit()

    return redirect(url_for('main.index'))