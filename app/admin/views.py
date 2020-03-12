# coding: utf-8
from . import admin
from flask import render_template


@admin.route("/")
def index():
    print('__name__',__name__)
    return render_template('admin/admin.html')  #返回home.html模板