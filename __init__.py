from flask import Flask, render_template, request, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']= 'ef7f9c363b428a622a04'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db= SQLAlchemy(app)