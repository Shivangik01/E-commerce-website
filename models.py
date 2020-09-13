from datetime import datetime
from __main__ import db

class User(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	username=db.Column(db.String(20), unique=True, nullable=False)
	email=db.Column(db.String(20), unique=True, nullable=False)
	mobileno=db.Column(db.Integer, unique=True, nullable=False)
	password=db.Column(db.String(20),  nullable=False)

	def __repr__(self):
		return f"User('{self.username}' , '{self.email}', '{self.mobileno}')"
