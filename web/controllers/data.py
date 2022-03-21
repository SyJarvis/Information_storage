# -*- coding: UTF-8 -*-
# @Time     : 2022/3/19 14:04
# @Author   : Runke Zhong
# @Software : PyCharm


from flask import Blueprint,send_from_directory
from application import app
route_data = Blueprint('data', __name__)


@route_data.route("/<path:filename>")
def index( filename ):
    return send_from_directory(  app.root_path ,filename )