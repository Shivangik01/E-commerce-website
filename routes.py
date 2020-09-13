

from models import User

@app.route('/index')
def index():
	return render_template('/index.html')

@app.route('/login')
def login():
	form= LoginForm()
	return render_template('/login.html', title='Login Form', form=form)

@app.route('/registration', methods=['GET', 'POST'])	
def registration():
	form= RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('index'))
	return render_template('registration.html', title='SignUp Form', form=form)

@app.route('/clothing')
def clothing():
	return render_template('/clothing.html')	

if __name__ == '__main__':
	app.run(debug=True)
