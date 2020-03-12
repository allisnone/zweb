# -*- coding:utf-8 -*-
#Author: allisnone

from flask import Blueprint
zip = Blueprint("zip",__name__
                  #template_folder='/opt/auras/templates/',   #指定模板路径
                  #static_folder='/opt/auras/flask_bootstrap/static/',#指定静态文件路
                  )
import app.zip.views