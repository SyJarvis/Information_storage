# -*- coding: UTF-8 -*-
# @Time     : 2021/10/31 17:41
# @Author   : Runke Zhong
# @Software : PyCharm

DEBUG = True
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "mysql://root:mysql0220@127.0.0.1:3306/bookmark_flask?charset=utf8mb4"
SQLALCHEMY_TRACK_MODIFICATIONS = True

REDIS_HOST = '125.25.1.147'
REDIS_PORT = 10010
REDIS_NO = 0

AUTH_COOKIE_NAME = "book_mark"

## 过滤Url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]