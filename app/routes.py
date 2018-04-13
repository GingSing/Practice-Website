from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.static.sql import UserSQL
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/home')
def home():
    all_user =UserSQL.select_all()
    return render_template('home.html', title='Home', users=all_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    new_user = User()
    if form.validate_on_submit():
        new_user.username = form.username.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        if form.password.data == form.confirm_password:
            new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('register.html', form=form)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')


@app.route('/browse', methods=['GET', 'POST'])
@login_required
def browse():
    users = UserSQL.select_all()
    return render_template('browse.html', users=users)


@app.route('/saved', methods=['GET', 'POSTS'])
@login_required
def saved():
    return render_template('saved.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
