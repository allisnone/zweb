# -*- coding:utf-8 -*-
#Author: allisnone

from . import admin as auth
from flask import render_template , url_for, session, redirect

from ..models import User , Login_Form , Register_Form , Article 
from flask_login import current_user , login_required , login_user , logout_user , user_logged_in
from ..func import *
from .func import *




@auth.route('/')
def index():
    return render_template('register.html')



@auth.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        dic=make_json_dic(301,user_username='annoyance',date=mcc_time(),info=mcc_info('you have already authenticated.'))
        return jsonify(dic)       
    else:
        if request.method=='POST':
            form=Register_Form()
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
        form=Login_Form()
        dic=form_analysis(form)
        if dic!=None:
            if request.method=='POST':
                username=dic['username']
                password=dic['password']
                user=User.query.filter_by(name=username).first()
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
            return render_template('login.html')



@auth.route('/logout',methods=['POST','GET'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        dic=make_json_dic(200,user_username=current_user.name,date=mcc_time(),info=mcc_info('logout success.'))
        return render_template('index.html')
    else:
        dic=make_json_dic(301,user_username=current_user.name,date=mcc_time(),info=mcc_info('you have login.'))
        return render_template('login.html')

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


@auth.route('/activate/')
def activate(token):
    if token !=None:
        if User.check_activate_token(token=token):
            dic=dict()
            dic['info']='activate success'
            return jsonify(dic)
        else:
            dic=dict()
            dic['info']='activate fail'
        return jsonify(dic)
    else:
        mcc_print('none')
