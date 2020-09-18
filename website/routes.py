from flask import render_template, request, Response, redirect, url_for, flash
from website import app, db, bcrypt
from website.forms import *
from website.models import *
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/index')
def index():
    items = Item.query.all()
    return render_template('/index.html', items=items)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password',
                  'danger')
    return render_template('/login.html', title='Login Form', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    mobile=form.mobile.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created for {form.username.data}!',
              'success')
        return redirect(url_for('index'))
    return render_template('registration.html', title='SignUp Form', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/category_wise', methods=['GET', 'POST'])
def category_wise(reqcategory):
    items = Item.query.filter_by(category=reqcategory).all()
    return render_template('/category_wise.html', items=items)


@app.route("/item_description/<int:itemid>", methods=['GET', 'POST'])
@login_required
def item_description(itemid):
    item = Item.query.filter(id == itemid).first()
    return render_template('/item_description.html', item=item)


@app.route('/view_cart', methods=['GET', 'POST'])
def view_cart():
    cart = Cart.query.filter_by(userid=current_user.id).all()
    return render_template('/view_cart.html', cart=cart)


@app.route('/view_cart/<int:itemid>/buy', methods=['GET', 'POST'])
def buy(itemid):
    item = Cart.query.filter_by(userid=current_user.id,
                                itemid=itemid,
                                status='C').first()
    item.status = 'B'
    db.session.commit()
    flash(f'Item has been added to your cart!', 'success')
    return redirect(url_for('view_cart'))


@app.route('/view_cart/<int:itemid>/remove', methods=['GET', 'POST'])
def remove(itemid):
    item = Cart.query.filter_by(userid=current_user.id,
                                itemid=itemid,
                                status='C').first()
    db.session.delete(item)
    db.session.commit()
    flash(f'Item has been successfully removed!', 'success')
    return redirect(url_for('view_cart'))


@app.route("/item_description/<int:item_id>/addtocart",
           methods=['GET', 'POST'])
@login_required
def addtocart(catitemid):
    cart = Cart(userid=current_user.id, itemid=catitemid, status='C')
    db.session.add(cart)
    db.session.commit()
    flash('Item successfully added to cart !!', 'success')
    return redirect(url_for('index'))
