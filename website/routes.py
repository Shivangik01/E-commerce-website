from flask import  render_template, request, Response, redirect, url_for, flash
from website import app,db,bcrypt
from website.forms import RegistrationForm, LoginForm
from website.models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/index')
def index():
	return render_template('/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form= LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user,remember=form.remember.data)
			return redirect(url_for('index'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('/login.html', title='Login Form', form=form)

@app.route('/registration', methods=['GET', 'POST'])	
def registration():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form= RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, mobile=form.mobile.data,password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been created for {form.username.data}!', 'success')
		return redirect(url_for('index'))
	return render_template('registration.html', title='SignUp Form', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/clothing')
def clothing():
	return render_template('/clothing.html')	


