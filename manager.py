# -*- coding:utf-8 -*-
#Author: allisnone

from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)  #运行flask HTTP 服务