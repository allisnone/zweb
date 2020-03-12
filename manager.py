# -*- coding:utf-8 -*-
#Author: allisnone

from app import app
from app.models import db

if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0',port=5000,debug=True)  #运行flask HTTP 服务