# -- coding: utf-8 --
# @Time : 2024/1/21 13:54
# @Author : JiahuaLInk
# @Email : 840132699@qq.com
# @File : room_handler.py
# @Software: PyCharm
# exts.py
from flask import request

from flask_socketio import Namespace, emit, join_room, leave_room


class ConnectManager(Namespace):
    # 用于存储房间信息，格式为 {room_name: {'users': [user1, user2], 'game_started': False}}

    def __init__(self, namespace):
        super().__init__(namespace)

    def on_connect(self):
        print(f"客户端已连接: {request.sid}")


    def on_disconnect(self):
        print(f"客户端已断开连接: {request.sid}")
        # self.leave_current_room()

