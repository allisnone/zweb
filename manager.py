# -*- coding:utf-8 -*-
#Author: allisnone

from app import app
from app.models import db
from app.admin.views import login_manager,csrf

if __name__ == "__main__":
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    app.run(host='0.0.0.0',port=5000,debug=True)  #运行flask HTTP 服务