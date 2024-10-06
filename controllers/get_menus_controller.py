from utils.response import response
from services.menus import menus

def get_menus_controller():
    data = menus()
    return response(data)