# -*- coding:utf-8 -*-
#Author: allisnone
from flask import Blueprint

# 1. url_prefix & static_folder & template_folder为可选参数。
# 2. 不定义template_folder，默认去主app配置的模板目录下查找模板（一般为templates）；
# 3. 如果定义了template_folder，且template_folder与templates的模板文件重名，优先使用templates的模板文件。
# 4. static_folder用法和template_folder类似。
# 5. 项目不大的话，尽量用主app默认的template_folder和static_folder。
#home = Blueprint('home', __name__, url_prefix='/home',template_folder='home_templates', static_folder='home_static')  
home = Blueprint("home",__name__
                #template_folder='/opt/auras/templates/',   #指定模板路径
                #static_folder='/opt/auras/flask_bootstrap/static/',#指定静态文件路
                )
import app.home.views