# -*- coding:utf-8 -*-
#Author: allisnone

from . import home
from flask import render_template

@home.route("/")
def index():
    print('__name__',__name__)
    return render_template('home/home.html')  #返回home.html模板