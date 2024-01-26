from flask import Flask
from flask_cors import CORS

from exts import socketio
from socket_manager.connect_handler import ConnectManager
from socket_manager.room_handler import RoomManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:74108520Ljh@localhost/pokemondb'  # 替换为你的数据库连接信息
CORS(app, support_credentials=True)
CORS(app, resources={r"/*": {"origins": "*"}})


def create_app(app):
    app.config['SECRET_KEY'] = 'liajiahua-key'
    socketio.init_app(app, cors_allowed_origins='*', asynz_mode='threading')
    socketio.on_namespace(ConnectManager('/'))
    socketio.on_namespace(RoomManager('/'))
    return app

if __name__ == '__main__':
    app = create_app(app)
    app.run(host='0.0.0.0', port=8889, debug=True)
