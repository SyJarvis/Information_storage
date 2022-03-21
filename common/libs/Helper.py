# -*- coding: UTF-8 -*-
# @Time     : 11/13/21 12:46 PM
# @Author   : Runke Zhong
# @Software : Pycharm

from flask import render_template, g
import datetime
import uuid



'''统一模板渲染方法'''
def ops_render(template, context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template, **context)


'''获取当前时间'''
def getCurrentDate(format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(format)


'''随机生成一个文件名'''
def getFileSalt():
    return str(uuid.uuid1())






