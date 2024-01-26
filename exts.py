# -- coding: utf-8 --
# @Time : 2024/1/21 13:45
# @Author : JiahuaLInk
# @Email : 840132699@qq.com
# @File : exts.py
# @Software: PyCharm
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS

cors = CORS()
db: SQLAlchemy = SQLAlchemy()
socketio = SocketIO()
