# -*- coding: UTF-8 -*-
# @Time     : 2021/10/31 17:49
# @Author   : Runke Zhong
# @Software : PyCharm


from flask import Blueprint, send_from_directory
from application import root_path

route_static = Blueprint("static_page", __name__)

