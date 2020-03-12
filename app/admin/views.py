# -*- coding:utf-8 -*-
#Author: allisnone

from . import admin as auth
from flask import render_template , url_for, session, redirect,request,jsonify
from ..models import User , LoginForm , RegisterForm ,db #, Article 
from flask_login import current_user , login_required , login_user , logout_user , user_logged_in,LoginManager
from flask_wtf.csrf import CsrfProtect
# use login manager to manage session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
# csrf protection
csrf = CsrfProtect()



@auth.route("/test")
def test():
    print('__name__',__name__)
    return render_template('admin/admin.html')  #返回home.html模板


@auth.route('/')
def register_index():
    return render_template('admin/register.html')

def make_json_dic(code,date=None,info=None):
    return {'code': code, 'date': date, 'info': info}

def mcc_time():
    return '2020-031-2'

def mcc_info(str):
    return str

def form_analysis(form):
    return {}

@auth.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        dic = make_json_dic(301,user_username='annoyance',date=mcc_time(),info=mcc_info('you have already authenticated.'))
        return jsonify(dic)       
    else:
        if request.method=='POST':
            form = Register_Form()
            if form.mcc_validate():
            #if form.validate_on_submit():
                name=form.username.data
                if form.password.data==form.re_password.data:
                    password=form.password.data
                    email=form.email.data               
                    if db_user_auth(name,password)==False:
                        if mail_auth(email):
                            user=User()
                            user.name=name
                            user.password=password
                            user.email=email
                            db.session.add(user)
                            db.session.commit()
                            token = user.generate_activate_token()
                            # 发送激活邮件到注册邮箱
                            send_mail(email, '账户激活', 'auth\\templates\\Life_Is_Strange_Artwork_5.jpg', token=token,username=name)
                            # 提示用户下一步操作
                            return render_template('login.html')
                        else:
                            dic=make_json_dic(301,user_username=name,date=mcc_time(),info=mcc_info('email type erro.'))
                            return jsonify(dic)
                            #return render_template('register.html')
                    else:
                        dic=make_json_dic(301,user_username=name,date=mcc_time(),info=mcc_info('the user is registered .'))
                        return jsonify(dic)
                        #return render_template('register.html')
                else:
                    dic=make_json_dic(301,user_username=name,date=mcc_time(),info=mcc_info('the password is not same.'))
                    return jsonify(dic)
                    #return render_template('register.html')
            else:
                dic=make_json_dic(301,user_username=name,date=mcc_time(),info=mcc_info('the form is not complete. '))
                return jsonify(dic)
                #return render_template('register.html')
        else:
            dic=make_json_dic(301,date=mcc_time(),info=mcc_info('the request is not supported.'))
            return jsonify(dic)
            #return render_template('register.html')


@auth.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        mcc_print("you are authenticated")
        dic=make_json_dic(200,user_username=current_user.name,date=mcc_time(),info='current user is authenticated.')
        return jsonify(dic)    
    else:       
        form=LoginForm()
        dic=form_analysis(form)
        if dic!=None:
            if request.method=='POST':
                username=dic['username']
                password=dic['password']
                user=User.query.filter_by(username=username).first()
                if user is not  None and password==user.password and user.confirmed==True:
                    session["username"]=username
                    session["password"]=password
                    login_user(user,True)
                    dic=make_json_dic(200,user_username=current_user.name,date=mcc_time(),info=mcc_info('current user is login.'))
                    return jsonify(dic)          
                else:
                    dic=make_json_dic(301,user_username=current_user.name,date=mcc_time(),info=mcc_info('authenticate fail.'))
                    return jsonify(dic)
            else:
                dic=make_json_dic(301,user_username=current_user.name,date=mcc_time(),info=mcc_info('authenticate fail.'))
                return render_template('login.html')
        else:
            dic=make_json_dic(404)
            return render_template('admin/login.html')



@auth.route('/logout',methods=['POST','GET'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        dic=make_json_dic(200,user_username=current_user.name,date=mcc_time(),info=mcc_info('logout success.'))
        return render_template('index.html')
    else:
        dic=make_json_dic(301,user_username=current_user.name,date=mcc_time(),info=mcc_info('you have login.'))
        return render_template('admin/login.html')

@auth.route('/activate/<token>')
def activate(token):
    if token !=None:
        if User.check_activate_token(self=current_user,token=token):
            dic=dict()
            dic['info']='activate success'
            return jsonify(dic)
        else:
            dic=dict()
            dic['info']='activate fail'
            return jsonify(dic)
    else:
        mcc_print('none')


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@auth.route('/')
@auth.route('/main')
@login_required
def main():
    return render_template(
        'admin/main.html', username=current_user.username)
    
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