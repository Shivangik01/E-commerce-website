from website import db,login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id=db.Column(db.Integer, primary_key=True)
	username=db.Column(db.String(20), unique=True, nullable=False)
	email=db.Column(db.String(20), unique=True, nullable=False)
	mobile=db.Column(db.Integer, unique=True, nullable=False)
	password=db.Column(db.String(20),  nullable=False)
#	items=db.relationship('Item',  )

	def __repr__(self):
		return f"User('{self.username}' , '{self.email}', '{self.mobile}')"



class Item(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	title=db.Column(db.String(20), unique=True, nullable=False)
	description=db.Column(db.String(1000), nullable=False)
	price=db.Column(db.Integer, nullable=False)
	size=db.Column(db.String(5), nullable=False)
	color=db.Column(db.String(10), nullable=False)
	number=db.Column(db.Integer, nullable=False)
	category=db.Column(db.String(20), nullable=False)
	subcategory=db.Column(db.String(20), nullable=False)
	img=db.Column(db.String(20), unique=True,nullable=False)

	def __repr__(self):
		return f"User('{self.title}' , '{self.description}', '{self.price}')"

