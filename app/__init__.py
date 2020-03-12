# -*- coding:utf-8 -*-
#Author: allisnone
from flask import Flask

app = Flask(__name__,
        template_folder='templates', #指定模板路径，可以是相对路径，也可以是绝对路径。 
        static_folder='static',  #指定静态文件前缀，默认静态文件路径同前缀
        #static_url_path='/opt/auras/static',     #指定静态文件存放路径。
         ) 
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
from app.zip import zip as zip_blueprint
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix="/admin")
app.register_blueprint(zip_blueprint,url_prefix="/zip")

