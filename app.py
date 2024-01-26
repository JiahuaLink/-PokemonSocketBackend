import os

from flask import Flask
from flask_cors import CORS

from exts import socketio
from socket_manager.connect_handler import ConnectManager
from socket_manager.room_handler import RoomManager

app = Flask(__name__)
CORS(app, support_credentials=True)
CORS(app, resources={r"/*": {"origins": "*"}})


def create_app(app):
    app.config['SECRET_KEY'] = 'liajiahua-key'
    # 使用 getenv 方法获取环境变量，如果没有设置，使用默认值
    database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI', '')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    socketio.init_app(app, cors_allowed_origins='*', async_mode='threading')
    socketio.on_namespace(ConnectManager('/'))
    socketio.on_namespace(RoomManager('/'))
    return app

if __name__ == '__main__':
    app = create_app(app)
    app.run(host='0.0.0.0', port=8889, debug=True)
