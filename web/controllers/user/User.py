# -*- coding: UTF-8 -*-
# @Time     : 11/15/21 4:04 PM
# @Author   : Runke Zhong
# @Software : Pycharm

from flask import Blueprint, request, jsonify, make_response, redirect, g
import json
from common.models.User import User
from common.libs.Helper import ops_render,getCurrentDate
from application import app, db
from common.libs.user.UserService import UserService



route_user = Blueprint("user_page", __name__)


@route_user.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return ops_render("/user/register.html")
    elif request.method == "POST":
        resp = {'code': 200, 'msg': '注册成功', 'data':{}}
        req = request.values
        username = req['username'] if 'username' in req else ''
        phone = req['phone'] if 'phone' in req else ''
        password1 = req['password1'] if 'password1' in req else ''
        password2 = req['password2'] if 'password2' in req else ''

        if username is None or len(username) < 1:
            resp['code'] = -1
            resp['msg'] = '请输入正确的用户名'
            return jsonify(resp)

        if phone is None or len(phone) != 11:
            resp['code'] = -1
            resp['msg'] = '请输入正确的手机号'
            return jsonify(resp)

        if password1 is None or len(password1) < 1:
            resp['code'] = -1
            resp['msg'] = '请输入符合规范的密码'
            return jsonify(resp)

        if password1 != password2:
            resp['code'] = -1
            resp['msg'] = '两次密码输入不一样'
            return jsonify(resp)

        try:
            user_info = User.query.filter_by(name=username).first()
        except Exception as e:
            print("数据库连接错误")
            resp['code'] = -1
            resp['msg'] = '数据库连接错误'
            return jsonify(resp)

        if user_info:
            resp['code'] = -1
            resp['msg'] = '此用户已注册'
            return jsonify(resp)

        user_info = User()
        user_info.name = username
        user_info.mobile = phone
        user_info.password = password1
        user_info.salt = ''
        user_info.created_time = getCurrentDate()
        user_info.updated_time = getCurrentDate()

        db.session.add(user_info)
        db.session.commit()

        return jsonify(resp)


@route_user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return ops_render('/user/login.html')
    elif request.method == "POST":
        resp = {'code': 200, 'msg': '登录成功', 'data':{}}
        req = request.values
        username = req['username'] if 'username' in req else ''
        password = req['password'] if 'password' in req else ''
        if username is None or len(username) < 1:
            resp['code'] = -1
            resp['msg'] = '请输入正确的用户名'
            return jsonify(resp)

        if password is None or len(password) < 6:
            resp['code'] = -1
            resp['msg'] = '请输入6位以上的密码'
            return jsonify(resp)

        try:
            user_info = User.query.filter_by(name=username).first()
        except Exception as e:
            print("数据库连接错误")
            resp['code'] = -1
            resp['msg'] = '没有此用户'
            return jsonify(resp)

        if not user_info:
            resp['code'] = -1
            resp['msg'] = '请输入正确的用户名或密码'
            return jsonify(resp)

        if user_info.password != password:
            resp['code'] = -1
            resp['msg'] = '请输入正确的用户名或密码'
            return jsonify(resp)

        response = make_response(json.dumps(resp))
        response.set_cookie(app.config['AUTH_COOKIE_NAME'], "%s#%s" %
                            (UserService.geneAuthCode(user_info), user_info.id), 60*60*24*120)

        print("登录成功")
        return response
