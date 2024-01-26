# -- coding: utf-8 --
# @Time : 2024/1/21 13:54
# @Author : JiahuaLInk
# @Email : 840132699@qq.com
# @File : socket_handler.py
# @Software: PyCharm
# exts.py
from flask import request

from flask_socketio import Namespace, emit, join_room, leave_room
rooms_info = {
    'RID': {
        'users': [],
        'game_started': False
    }
}

class WebSocketManager(Namespace):
    # 用于存储房间信息，格式为 {room_name: {'users': [user1, user2], 'game_started': False}}

    def __init__(self, namespace):
        super().__init__(namespace)

    def on_connect(self):
        print(f"客户端已连接: {request.sid}")

    def on_rooms_list(self):
        print('on_rooms_list事件', rooms_info)
        emit('rooms_list', rooms_info)

    def on_disconnect(self):
        print(f"客户端已断开连接: {request.sid}")
        # self.leave_current_room()

    def on_create_room(self, data):
        print('create_room', data)
        room_name = data.get('room_name')
        join_room(room_name)
        rooms_info[room_name] = {'users': [], 'game_started': False}
        print('成功创建房间', rooms_info)
        emit('room_created', {'room_name': room_name, 'message': '成功创建房间。'})
        emit('rooms_list', rooms_info)

    def on_join_room(self, data):
        room_name = data.get('room_name')
        print('join_room', room_name)
        if room_name in rooms_info and len(rooms_info[room_name]['users']) < 2:
            join_room(room_name)
            rooms_info[room_name]['users'].append(request.sid)
            emit('room_joined', rooms_info[room_name])
            self.update_room_info(room_name)
        else:
            print('房间已满或不存在')
            emit('room_full', {'message': '房间已满或不存在。'})

    def on_leave_room(self, room_name):
        print('leave_room', room_name)
        self.leave_current_room(room_name)

    def leave_current_room(self, roomName):
        for key, value in rooms_info.items():

            current_room = rooms_info[key]
            if request.sid in current_room['users']:
                leave_room(roomName)
                rooms_info[roomName]['users'].remove(request.sid)
                self.update_room_info(roomName)
        emit('room_left')
        emit('rooms_list', rooms_info)

    def update_room_info(self, room_name):
        room_info = rooms_info.get(room_name, {})
        emit('update_room_info', {'room_name': room_name, 'users': room_info.get('users', []),
                                  'game_started': room_info.get('game_started', False)}, room=room_name)

    def on_start_game(self, room_name):
        if room_name in rooms_info and len(rooms_info[room_name]['users']) == 2:
            rooms_info[room_name]['game_started'] = True
            emit('game_started', {'room_name': room_name, 'message': '游戏已开始！'}, room=room_name)
            emit('game_room_info',rooms_info[room_name],room=room_name)
        else:
            emit('game_start_failed', {'message': '游戏开始失败。请确保房间中有两名玩家。'})

    def on_send_message(self, data):
        room_name = data.get('room_name')
        content = data.get('content')
        sender = request.sid
        emit('chat_message', {'sender': sender, 'content': content}, room=room_name)