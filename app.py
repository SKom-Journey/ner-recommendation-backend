from flask import Flask
from controllers.get_menu import get_menu_controller

app = Flask(__name__)

@app.route('/menus')
def get_menu():
    return get_menu_controller()

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
