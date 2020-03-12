# -*- coding:utf-8 -*-
#Author: allisnone

from . import admin
from flask import render_template


@admin.route("/")
def index():
    print('__name__',__name__)
    return render_template('admin/admin.html')  #返回home.html模板

"""
# -*- coding: utf-8 -*-
# Author: allisnone
#https://blog.csdn.net/yy19890521/article/details/81486051
from forms import LoginForm
from flask_wtf.csrf import CsrfProtect
from model import User
from flask_login import login_user, login_required
from flask_login import LoginManager, current_user
from flask_login import logout_user
 
app = Flask(__name__)
 
app.secret_key = os.urandom(24)
 
# use login manager to manage session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)
 
# 这个callback函数用于reload User object，根据session中存储的user id
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
 
 
# csrf protection
csrf = CsrfProtect()
csrf.init_app(app)
 
@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = request.form.get('username', None)
        password = request.form.get('password', None)
        remember_me = request.form.get('remember_me', False)
        user = User(user_name)
        if user.verify_password(password):
            login_user(user, remember=remember_me)
            return redirect(request.args.get('next') or url_for('main'))
    return render_template('login.html', title="Sign In", form=form)
    

@app.route('/')
@app.route('/main')
@login_required
def main():
    return render_template(
        'main.html', username=current_user.username)
    
"""   