from utils.response import response
from services.carts import create_cart

def create_cart_controller(json: dict):
    return response(create_cart(json['user_id'], json['menu_id'], json.get('note', None)))