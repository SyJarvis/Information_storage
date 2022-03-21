# -*- coding: UTF-8 -*-
# @Time     : 2021/10/31 17:45
# @Author   : Runke Zhong
# @Software : PyCharm


from flask import Blueprint, render_template, g, send_from_directory
from application import app

route_index = Blueprint("index_page", __name__)

@route_index.route("/<path:filename>")
def index( filename ):
    return send_from_directory(  app.root_path ,filename )