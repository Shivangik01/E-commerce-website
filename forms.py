from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username=StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email=StringField('Email', validators=[DataRequired(),Email() ])
	mobileno=StringField('Mobile Number', validators=[DataRequired(), Length(min=10, max=10)])
	password=PasswordField('Password', validators=[DataRequired()])
	confirmpassword=PasswordField('Confirm Password', validators=[DataRequired()])
	submit=SubmitField('Signup')


class LoginForm(FlaskForm):

	email=StringField('Email', validators=[DataRequired(),Email() ])
	password=PasswordField('Password', validators=[DataRequired()])
	remember=BooleanField('Remember Me')
	submit=SubmitField('Login')