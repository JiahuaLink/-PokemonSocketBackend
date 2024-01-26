from flask import Flask
from flask_cors import CORS

from exts import socketio
from socket_manager.socket_handler import WebSocketManager

app = Flask(__name__)

CORS(app, support_credentials=True)
CORS(app, resources={r"/*": {"origins": "*"}})


def create_app(app):
    app.config['SECRET_KEY'] = 'liajiahua-key'
    socketio.init_app(app, cors_allowed_origins='*', asynz_mode='threading')
    socketio.on_namespace(WebSocketManager('/'))
    return app


if __name__ == '__main__':
    app = create_app(app)
    app.run(host='0.0.0.0', port=8889, debug=True)
