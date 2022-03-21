# -*- coding: UTF-8 -*-
# @Time     : 2021/10/31 17:31
# @Author   : Runke Zhong
# @Software : PyCharm

from application import app, manager
from flask_script import Server
import www

manager.add_command("runserver", Server(host=app.config['SERVER_HOST'], port=app.config['SERVER_PORT'], use_reloader=True, use_debugger=True))


def main():
    manager.run()

if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        print("error")