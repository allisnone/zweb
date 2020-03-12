# -*- coding:utf-8 -*-
#Author: allisnone

from . import zip
from flask import render_template


@zip.route("/")
def index():
    print('__name__',__name__)
    return render_template('zip/zip.html')  #返回home.html模板