# -*- coding: UTF-8 -*-
# @Time     : 11/16/21 1:33 PM
# @Author   : Runke Zhong
# @Software : Pycharm

import hashlib, base64


class UserService():


    @staticmethod
    def geneAuthCode(user_info):
        m = hashlib.md5()
        str = "%s-%s-%s" % (user_info.name, user_info.password, user_info.salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()