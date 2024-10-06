from flask import Flask
from controllers.get_menu_recommendation_controller import get_menu_recommendation_controller
from controllers.get_menus_controller import get_menus_controller
from dotenv import load_dotenv
from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin

load_dotenv()

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins=['http://localhost:5173'])

@app.get('/menus')
def get_menu():
    return get_menus_controller()

@socketio.on('menu_recommendation')
def menu_recommendation(text):
    print(text)
    recommendation = get_menu_recommendation_controller(text)
    emit('menu_recommendation_response', recommendation)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=8080, host='0.0.0.0')
