# -*- coding:utf-8 -*-
#Author: allisnone
from . import zip
from flask import render_template

@zip.route("/")
def zip_upload_file():
    print('__name__',__name__)
    return render_template('zip/zip.html',files='')  #返回zip.html模板

@zip.route("/test")
def zip_upload_file1():
    print('__name__',__name__)
    return render_template('zip/zip_test.html',files='')  #返回zip.html模板