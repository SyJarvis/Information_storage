# -*- coding: UTF-8 -*-
# @Time     : 2021/10/31 17:31
# @Author   : Runke Zhong
# @Software : PyCharm

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
import redis

pymysql.install_as_MySQLdb()


class Application(Flask):

    def __init__(self, import_name, template_folder=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, static_folder=None)
        self.config.from_pyfile("config/base_setting.py")
        if 'ops_config' in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])
        db.init_app(self)


root_path = os.getcwd()
db = SQLAlchemy()
app = Application(__name__, template_folder=root_path + "/web/templates")
# 根路径
app.root_path = root_path
manager = Manager(app)
# Redis数据库
r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])


"""函数模板"""
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.add_template_global(UrlManager.buildFileUrl, 'buildFileUrl')



