from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Phone
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login successful!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('web_views.index'))
            else:
                flash('Incorrect password!', category='error')
        else:
            flash('Email does not exist!', category='error')

    return render_template('login.jinja2', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('email must be more than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be more than 1 character.', category='error')
        elif password1 != password2:
            flash('password is not the same', category='error')
        elif len(password1) < 7:
            flash('password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # I deleted this login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('web_views.index'))

    return render_template('sign_up.jinja2', user=current_user)


@auth.route('/add_contact', methods=['GET', 'POST'])
@login_required
def add_contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        mobile_no = request.form.get('mobile_no')
        phone_no = request.form.get('phone_no')
        birth_date = request.form.get('birth_date')
        email = request.form.get('email')

        if first_name == '':
            flash('Please enter first name!', category='error')
        elif len(first_name) < 1:
            flash('Name is too short!', category='error')
        elif mobile_no == '':
            flash('Please enter mobile number', category='error')
        elif len(mobile_no) < 11:
            flash('Mobile number not complete')
        else:
            new_contact = Phone(first_name=first_name, last_name=last_name, mobile_no=mobile_no, phone_no=phone_no,
                                birth_date=birth_date, email=email, user_id=current_user.id)
            db.session.add(new_contact)
            db.session.commit()
            flash('Contact added!', category='success')
            return redirect(url_for('web_views.index'))

    return render_template('add_contact.jinja2', user=current_user)

