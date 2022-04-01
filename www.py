# -*- coding: UTF-8 -*-
# @Time     : 2021/10/31 17:31
# @Author   : Runke Zhong
# @Software : PyCharm
from application import app


'''
蓝图功能，对所有的url进行蓝图功能配置
'''

from web.controllers.index import route_index
from web.controllers.static import route_static
from web.controllers.user.User import route_user
from web.controllers.file.UploadFile import route_file
from web.controllers.data import route_data


app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_static, url_prefix="/static")
app.register_blueprint(route_user, url_prefix="/user")
app.register_blueprint(route_file, url_prefix="/file")
app.register_blueprint(route_data, url_prefix='/data')

