# -*- coding:utf-8 -*-
#Author: allisnone

from app import app
from app.models import db

if __name__ == "__main__":
    #DB的连接词
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    #默认True，SQLAlchemy会记录下对象的变动，可以理解成写log
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.run(host='0.0.0.0',port=5000,debug=True)  #运行flask HTTP 服务