# -*- coding: UTF-8 -*-
# @Time     : 2021/10/31 17:37
# @Author   : Runke Zhong
# @Software : PyCharm


import time
from application import app, root_path

class UrlManager(object):

    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        release_version = app.config.get("RELEASE_VERSION")
        ver = "%s"%(int(time.time())) if not release_version else release_version
        path = "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl(path)

    @staticmethod
    def buildImageUrl(path):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['UPLOAD']['prefix_url'] + path
        return url

    @staticmethod
    def buildFileUrl(path):
        release_version = app.config.get("RELEASE_VERSION")
        ver = "%s"%(int(time.time())) if not release_version else release_version
        path = path + "?ver=" + ver
        return UrlManager.buildUrl(path)




