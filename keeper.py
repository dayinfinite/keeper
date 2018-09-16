#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
""" 
 @desc:  
 @author: dayinfinte
 @date: 2018/01/05
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49 
 """

from flask import Flask, jsonify
from flask_apscheduler import APScheduler
import simplejson as json
from log import logger



@app.route("/", methods=["GET"])
def index():
    return "Hello, World"




if __name__ == "__main__":


    app = Flask(__name__)
    scheduler =APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)
