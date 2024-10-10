from flask import Flask, request
from controllers.get_menu_recommendation_controller import get_menu_recommendation_controller
from controllers.get_menus_controller import get_menus_controller
from dotenv import load_dotenv
from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from controllers.get_qr_controller import get_qr_controller
from controllers.get_qrs_controller import get_qrs_controller
from controllers.create_qr_controller import create_qr_controller
from controllers.delete_qr_controller import delete_qr_controller
from controllers.create_order_controller import create_order_controller
from controllers.get_orders_controller import get_orders_controller

load_dotenv()

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins=['http://localhost:5173'])

@app.get('/orders')
def get_orders():
    return get_orders_controller()

@app.post('/orders')
def create_order():
    return create_order_controller(request.get_json())

@app.get('/qrs/<qr_id>')
def get_qr(qr_id: str):
    return get_qr_controller(qr_id)

@app.get('/qrs')
def get_qrs():
    return get_qrs_controller()

@app.post('/qrs')
def create_qr():
    return create_qr_controller(request.get_json())

@app.delete('/qrs/<qr_id>')
def delete_qr(qr_id: str):
    return delete_qr_controller(qr_id)

@app.get('/menus')
def get_menu():
    return get_menus_controller(request.args.get('keyword', type=str))

@socketio.on('menu_recommendation')
def menu_recommendation(text):
    print(text)
    recommendation = get_menu_recommendation_controller(text)
    emit('menu_recommendation_response', recommendation)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=8080, host='0.0.0.0')
