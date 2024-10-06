from flask import Flask
from controllers.get_menu_recommendation_controller import get_menu_recommendation_controller
from controllers.get_menus_controller import get_menus_controller
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.get('/menus')
def get_menu():
    return get_menus_controller()

@app.route('/recommendation')
def get_menu_recommendation():
    return get_menu_recommendation_controller()

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
