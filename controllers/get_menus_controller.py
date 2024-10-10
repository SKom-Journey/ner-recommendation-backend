from utils.response import response
from services.menus import menus

def get_menus_controller(keyword: str):
    return response(menus(keyword))