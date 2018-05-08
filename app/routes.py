from app import app, db
from flask import render_template, flash, redirect, url_for, request, jsonify
from app.forms import LoginForm, RegistrationForm, PostForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.static.sql import UserSQL, insert, select, delete, update
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/home')
def home():
    all_user = UserSQL.select_all()
    posts_daily = select.select_daily_posts().fetchall()
    print(posts_daily)
    daily = []
    # for thing in posts_daily:
    #     print(thing)
    #     daily.append(dict(thing))
    posts_weekly = select.select_weekly_posts().fetchall()
    weekly = []
    for thing in posts_weekly:
        weekly.append(dict(thing))
    return render_template('home.html', title='Home', users=all_user, daily_posts=daily, weekly_posts=weekly)


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
        else:
            flash("Passwords do not match.")
        db.session.add(new_user)
        db.session.commit()
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('register.html', form=form)


@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        insert.create_post(form.title.data, form.subtitle.data, form.content.data, str(User.get_id(current_user)))
        return redirect(url_for('home'))
    return render_template('post.html', form=form)


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


@app.route('/get_weekly_posts/<post_id>', methods=["GET"])
@login_required
def get_weekly_posts(post_id):
    post_weekly = select.select_weekly_posts(post_id).fetchone()
    d = dict(post_weekly)
    return jsonify(d)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
