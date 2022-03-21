# -*- coding: UTF-8 -*-
# @Time     : 11/13/21 12:56 PM
# @Author   : Runke Zhong
# @Software : Pycharm


from flask import request, redirect, g
from application import app
from common.libs.user.UserService import UserService
from common.libs.UrlManager import UrlManager
from common.models.User import User
import re


@app.before_request
def before_request():
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path

    """
    如果登录页面也需要登录的话，就陷入死循环了
    """

    pattern = re.compile('%s' % '|'.join(ignore_check_login_urls))
    if pattern.match(path):
        return

    user_info= check_login()
    g.current_user = None
    if user_info:
        g.current_user = user_info
    app.logger.info(user_info)
    pattern = re.compile()



'''
判断用户是否已经登录
'''
def check_login():
    cookies = request.cookies
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else ''
    app.logger.info(auth_cookie)
    if auth_cookie is None:
        return False
    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(id=auth_info[1]).first()
    except Exception as e:
        return False

    if user_info is None:
        return False

    if user_info.status != 1:
        return False
    return user_info


